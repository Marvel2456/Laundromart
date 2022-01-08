from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard, name='dashboard'),
    path('pos', views.Pos, name='pos'),
    path('pickup', views.Pickup, name='pickup'),
    path('sales', views.SalesRecord, name='sales'),
    path('cart', views.CheckoutDetails, name='cart'),
    path('update_item', views.updateItem, name='update_item')
]