from rest_framework import serializers
from .models import Order , OrderStatus

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id' , 'user' , 'product' , 'quantity']
        depth = 1

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'