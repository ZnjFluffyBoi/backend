from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class ProductView(APIView):

    def get(self , request , format=None):
        products = Product.objects.all().order_by('-id')
        serializer = ProductSerializer(products , many=True)
        return Response({'ok': True , 'data': serializer.data} , status=200)

    def post(self , request , format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True , 'data': serializer.data} , status=200)
        return Response({'ok': False , 'errors': serializer.errors})

    def patch(self , request , format=None):
            
            product_instance = Product.objects.get(id=request.data['id'])
            serializer = ProductSerializer(product_instance , data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'ok': True, 'data': serializer.data}, status=200)
        
            return Response({'ok': False, 'message': 'something went wrong'})

    def delete(self , request , format=None):
        product_instance = Product.objects.get(id=request.data['id'])

        product_instance.delete()
        return Response("Deleted")
