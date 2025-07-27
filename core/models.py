from django.db import models
from django.contrib.auth.models import User

class Branch(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    gps_location = models.CharField(max_length=255)  # Could use a PointField with GeoDjango

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=255)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username

class Order(models.Model):
    PICKUP = 'pickup'
    DELIVERY = 'delivery'
    ORDER_TYPE_CHOICES = [
        (PICKUP, 'Pick Up'),
        (DELIVERY, 'Delivery'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('ready', 'Ready'),
        ('out_for_delivery', 'Out for Delivery'),
        ('completed', 'Completed'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    order_type = models.CharField(max_length=10, choices=ORDER_TYPE_CHOICES)
    address = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.customer}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
