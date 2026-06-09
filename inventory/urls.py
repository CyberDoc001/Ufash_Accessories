from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('catalog/', views.ProductCatalogView.as_view(), name='catalog'),
    path('product/add/', views.AddProductView.as_view(), name='add_product'),
    path('product/<int:pk>/edit/', views.EditProductView.as_view(), name='edit_product'),
    path('product/<int:pk>/add-to-cart/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart/<int:pk>/remove/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('receipt/<int:sale_id>/', views.ReceiptView.as_view(), name='receipt'),
    path('sales-report/', views.SalesReportView.as_view(), name='sales_report'),
    path('restock-alerts/', views.RestockAlertsView.as_view(), name='restock_alerts'),
    path('alert/<int:pk>/resolve/', views.ResolveAlertView.as_view(), name='resolve_alert'),
    path('categories/', views.ManageCategoriesView.as_view(), name='categories'),
    path('category/add/', views.AddCategoryView.as_view(), name='add_category'),
]

