from django.contrib import admin
from .models import Branch, Product, Customer, Order, OrderItem

admin.site.register(Branch)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
