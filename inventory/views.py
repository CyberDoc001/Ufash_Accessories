from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db.models import Q, Sum, F
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from datetime import timedelta
import json
from decimal import Decimal

from .models import Product, Category, Sale, SaleItem, RestockAlert
from .forms import ProductForm, CategoryForm, SearchForm, UserRegistrationForm, UserLoginForm


class DashboardView(View):
    def get(self, request):
        context = {
            'total_products': Product.objects.filter(is_active=True).count(),
            'low_stock_products': Product.objects.filter(is_active=True, quantity__lte=F('minimum_stock')).count(),
            'total_categories': Category.objects.count(),
            'active_alerts': RestockAlert.objects.filter(status='active').count(),
            'today_sales': Sale.objects.filter(sale_date=timezone.now().date()).aggregate(
                total=Sum('total_amount'), count=Sum('items_count')
            ),
            'recent_alerts': RestockAlert.objects.filter(status='active')[:5],
        }
        return render(request, 'inventory/dashboard.html', context)


class ProductCatalogView(View):
    @method_decorator(login_required(login_url='accounts:login'))
    def get(self, request):
        products = Product.objects.filter(is_active=True).select_related('category')
        search_form = SearchForm(request.GET)
        
        if request.GET.get('query'):
            query = request.GET.get('query')
            products = products.filter(
                Q(name__icontains=query) | Q(sku__icontains=query)
            )
        
        if request.GET.get('category'):
            category_id = request.GET.get('category')
            products = products.filter(category_id=category_id)

        context = {
            'products': products,
            'search_form': search_form,
            'categories': Category.objects.all(),
        }
        return render(request, 'inventory/catalog.html', context)


class AddProductView(View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'inventory/add_product.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('inventory:catalog')
        return render(request, 'inventory/add_product.html', {'form': form})

class EditProductView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=product)
        return render(request, 'inventory/edit_product.html', {'form': form, 'product': product})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('inventory:catalog')
        return render(request, 'inventory/edit_product.html', {'form': form, 'product': product})


class CartView(View):
    @method_decorator(login_required(login_url='accounts:login'))
    def get(self, request):
        cart = request.session.get('cart', {})
        cart_items = []
        total_amount = Decimal('0')
        surcharge = Decimal('100')

        for product_id, quantity in cart.items():
            try:
                product = Product.objects.get(id=product_id)
                unit_price = product.price + surcharge
                subtotal = unit_price * quantity
                cart_items.append({
                    'product': product,
                    'quantity': quantity,
                    'unit_price': unit_price,
                    'subtotal': subtotal,
                })
                total_amount += subtotal
            except Product.DoesNotExist:
                continue

        context = {
            'cart_items': cart_items,
            'total_amount': total_amount,
        }
        return render(request, 'inventory/cart.html', context)


class AddToCartView(View):
    @method_decorator(login_required(login_url='accounts:login'))
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        quantity = int(request.POST.get('quantity', 1))

        if quantity > product.quantity:
            messages.error(request, f'Not enough stock. Available: {product.quantity}')
            return redirect('inventory:cart')

        cart = request.session.get('cart', {})
        product_id = str(pk)

        if product_id in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity

        request.session['cart'] = cart
        messages.success(request, f'Added {quantity} x {product.name} to cart')
        return redirect('inventory:cart')


class RemoveFromCartView(View):
    @method_decorator(login_required(login_url='accounts:login'))
    def post(self, request, pk):
        cart = request.session.get('cart', {})
        product_id = str(pk)
        
        if product_id in cart:
            del cart[product_id]
            request.session['cart'] = cart
            messages.success(request, 'Item removed from cart')
        
        return redirect('inventory:cart')


class CheckoutView(View):
    @method_decorator(login_required(login_url='accounts:login'))
    def post(self, request):
        cart = request.session.get('cart', {})
        
        if not cart:
            messages.error(request, 'Cart is empty')
            return redirect('inventory:cart')

        total_amount = Decimal('0')
        items_count = 0
        sale_items = []

        try:
            for product_id, quantity in cart.items():
                product = Product.objects.get(id=product_id)
                
                if quantity > product.quantity:
                    messages.error(request, f'Insufficient stock for {product.name}')
                    return redirect('inventory:cart')

                surcharge = Decimal('100')
                unit_price = product.price + surcharge
                subtotal = unit_price * quantity
                total_amount += subtotal
                items_count += quantity

                sale_items.append({
                    'product': product,
                    'quantity': quantity,
                    'unit_price': unit_price,
                    'subtotal': subtotal,
                })

                product.quantity -= quantity
                product.save()

                if product.is_low_stock():
                    RestockAlert.objects.create(
                        product=product,
                        current_stock=product.quantity,
                        minimum_stock=product.minimum_stock,
                    )

            sale = Sale.objects.create(
                total_amount=total_amount,
                items_count=items_count,
            )

            for item in sale_items:
                SaleItem.objects.create(
                    sale=sale,
                    product=item['product'],
                    quantity=item['quantity'],
                    unit_price=item['unit_price'],
                    subtotal=item['subtotal'],
                )

            request.session['cart'] = {}
            messages.success(request, 'Sale completed successfully!')
            return redirect('inventory:receipt', sale_id=sale.id)

        except Product.DoesNotExist:
            messages.error(request, 'Product not found')
            return redirect('inventory:cart')


class ReceiptView(View):
    def get(self, request, sale_id):
        sale = get_object_or_404(Sale, id=sale_id)
        context = {'sale': sale}
        return render(request, 'inventory/receipt.html', context)


class SalesReportView(View):
    @method_decorator(login_required(login_url='accounts:login'))
    def get(self, request):
        date_filter = request.GET.get('date_filter', 'today')
        today = timezone.now().date()

        if date_filter == 'today':
            sales = Sale.objects.filter(sale_date=today)
        elif date_filter == 'week':
            week_ago = today - timedelta(days=7)
            sales = Sale.objects.filter(sale_date__gte=week_ago)
        elif date_filter == 'month':
            month_ago = today - timedelta(days=30)
            sales = Sale.objects.filter(sale_date__gte=month_ago)
        else:
            sales = Sale.objects.all()

        total_revenue = sales.aggregate(total=Sum('total_amount'))['total'] or Decimal('0')
        total_items = sales.aggregate(total=Sum('items_count'))['total'] or 0

        context = {
            'sales': sales,
            'total_revenue': total_revenue,
            'total_items': total_items,
            'date_filter': date_filter,
        }
        return render(request, 'inventory/sales_report.html', context)


class RestockAlertsView(View):
    @method_decorator(login_required(login_url='accounts:login'))
    def get(self, request):
        alerts = RestockAlert.objects.filter(status='active').select_related('product')
        context = {'alerts': alerts}
        return render(request, 'inventory/restock_alerts.html', context)


class ResolveAlertView(View):
    @method_decorator(login_required(login_url='accounts:login'))
    def post(self, request, pk):
        alert = get_object_or_404(RestockAlert, pk=pk)
        alert.status = 'resolved'
        alert.resolved_at = timezone.now()
        alert.save()
        messages.success(request, 'Alert marked as resolved')
        return redirect('inventory:restock_alerts')


class ManageCategoriesView(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(request, 'inventory/categories.html', context)


class AddCategoryView(View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'inventory/add_category.html', {'form': form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully!')
            return redirect('inventory:categories')
        return render(request, 'inventory/add_category.html', {'form': form})


class UserRegistrationView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('inventory:dashboard')
        form = UserRegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful! Please login with your credentials.')
            login(request, user)
            return redirect('inventory:dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
        return render(request, 'accounts/register.html', {'form': form})


class UserLoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('inventory:dashboard')
        form = UserLoginForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                remember_me = form.cleaned_data.get('remember_me')
                if not remember_me:
                    request.session.set_expiry(0)
                messages.success(request, f'Welcome back, {user.first_name or user.username}!')
                next_url = request.GET.get('next', 'inventory:dashboard')
                return redirect(next_url)
            else:
                messages.error(request, 'Invalid username or password.')
        return render(request, 'accounts/login.html', {'form': form})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('accounts:login')


class UserProfileView(View):
    @method_decorator(login_required(login_url='accounts:login'))
    def get(self, request):
        user = request.user
        context = {
            'user': user,
            'member_since': user.date_joined,
        }
        return render(request, 'accounts/profile.html', context)
