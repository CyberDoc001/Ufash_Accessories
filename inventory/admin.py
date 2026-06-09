from django.contrib import admin
from django.db import models as dj_models
from django.forms import NumberInput
from .models import Category, Product, Sale, SaleItem, RestockAlert


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name']
    list_filter = ['created_at']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    formfield_overrides = {
        dj_models.DecimalField: {'widget': NumberInput(attrs={'step': '0.01', 'min': '0', 'placeholder': '₦0.00'})}
    }
    list_display = ['name', 'sku', 'category', 'price_display', 'quantity', 'minimum_stock', 'is_active']
    list_filter = ['category', 'is_active', 'created_at']
    search_fields = ['name', 'sku']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Product Information', {
            'fields': ('name', 'sku', 'category', 'description', 'image')
        }),
        ('Pricing & Stock', {
            'fields': ('price', 'quantity', 'minimum_stock')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    @admin.display(ordering='price', description='Price (₦)')
    def price_display(self, obj):
        return f'₦{obj.price:,.2f}'


class SaleItemInline(admin.TabularInline):
    model = SaleItem
    readonly_fields = ['product', 'quantity', 'unit_price_display', 'subtotal_display']
    fields = ['product', 'quantity', 'unit_price_display', 'subtotal_display']
    extra = 0
    can_delete = False

    @admin.display(description='Unit Price (₦)')
    def unit_price_display(self, obj):
        return f'₦{obj.unit_price:,.2f}'

    @admin.display(description='Subtotal (₦)')
    def subtotal_display(self, obj):
        return f'₦{obj.subtotal:,.2f}'


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['id', 'sale_date', 'sale_time', 'total_amount_display', 'items_count']
    list_filter = ['sale_date', 'created_at']
    readonly_fields = ['sale_date', 'sale_time', 'created_at']
    inlines = [SaleItemInline]
    date_hierarchy = 'sale_date'

    @admin.display(ordering='total_amount', description='Total Amount (₦)')
    def total_amount_display(self, obj):
        return f'₦{obj.total_amount:,.2f}'


@admin.register(RestockAlert)
class RestockAlertAdmin(admin.ModelAdmin):
    list_display = ['product', 'current_stock', 'minimum_stock', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    readonly_fields = ['created_at', 'resolved_at']
    search_fields = ['product__name']
