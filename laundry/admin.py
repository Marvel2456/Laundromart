from django.contrib import admin
from .models import Laundry, Order, OrderItem

# Register your models here.
admin.site.register(Laundry),
admin.site.register(Order),
admin.site.register(OrderItem),

