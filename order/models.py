from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.

class OrderStatus(models.Model):
    name = models.CharField(max_length=200 , unique=True)

    def __str__(self):
        return f"{self.pk} - {self.name}"

class Order(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=300 , blank=True , null=True)

    def __str__(self):
        return f'{self.status} , {self.product} , {self.quantity} , {self.shipping_address}'
    
#    {
#         "user": 1,    <user_id>
#         "product": 1, <productID>
#         "quantity": 2, <INT>
#         "status": 1   <INT>
#     }

    