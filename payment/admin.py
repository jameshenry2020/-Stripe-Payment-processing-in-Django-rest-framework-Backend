from django.contrib import admin
from .models import Product,PaymentHistory
# Register your models here.

admin.site.register(Product)
admin.site.register(PaymentHistory)