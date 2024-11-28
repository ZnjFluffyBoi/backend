from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderSerializer , OrderStatusSerializer
from .models import Order
# Create your views here.

class OrderView(APIView):
    def get(self, request):
        items = Order.objects.all().exclude(status__name="cart")
        serializer = OrderSerializer(items , many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True , 'data': serializer.data} , status=200)
        return Response({'ok': False , 'errors': serializer.errors})
    
    def patch(self, request):
        product_instance = Order.objects.get(id=request.data['id'])
        serializer = OrderSerializer(product_instance , data=request.data, partial=True)
        if serializer.is_valid():
                serializer.save()
                return Response({'ok': True, 'data': serializer.data}, status=200)
        
    def delete(self, request):
        product_instance = Order.objects.get(id=request.data['id'])

        product_instance.delete()
        return Response("Deleted")


class OrderStatusView(APIView):
    def get(self, request):
        items = Order.objects.all().exclude(status__name="cart")
        serializer = OrderStatusSerializer(items , many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = OrderStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True , 'data': serializer.data} , status=200)
        return Response({'ok': False , 'errors': serializer.errors})

    def patch(self, request):
        product_instance = Order.objects.get(id=request.data['id'])
        serializer = OrderStatusSerializer(product_instance , data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True, 'data': serializer.data}, status=200)

    def delete(self, request):
        product_instance = Order.objects.get(id=request.data['id'])

        product_instance.delete()
        return Response("Deleted")


class CartView(APIView):
    def get(self,request):
        items = Order.objects.all().filter(status__name="cart")
        serializer = OrderSerializer(items , many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True , 'data': serializer.data} , status=200)
        return Response({'ok': False , 'errors': serializer.errors})

    def patch(self, request):
        product_instance = Order.objects.get(id=request.data['id'])
        serializer = OrderSerializer(product_instance , data=request.data, partial=True)
        if serializer.is_valid():
                serializer.save()
                return Response({'ok': True, 'data': serializer.data}, status=200)
        
    def delete(self, request):
        product_instance = Order.objects.get(id=request.data['id'])

        product_instance.delete()
        return Response("Deleted")