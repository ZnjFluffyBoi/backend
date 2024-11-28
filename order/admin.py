from django.contrib import admin
from .models import Order , OrderStatus
# Register your models here.
admin.site.register(OrderStatus)
admin.site.register(Order)