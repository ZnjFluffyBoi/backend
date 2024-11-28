from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User
from .serializer import UserSerializer
from rest_framework.parsers import FormParser , MultiPartParser, JSONParser

class UserView(APIView):
    # parser_classes =[FormParser , MultiPartParser , JSONParser]
    def get(self , request ,  format=None):
        users = User.objects.all()
        serializer = UserSerializer(users , many=True)
        return Response({'ok': True , 'data': serializer.data} , status=200)

    def post(self , request , format=None):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            return Response({'ok': True , 'data' : serializer.data} , status=200)
        return Response({'ok': False , 'errors': serializer.errors},status=400)
    
    def patch(self , request , format=None):
        try:
            user_instance = User.objects.get(id=request.data['id'])
            if user_instance.check_password(request.data['old_password']):
                request.data.pop('old_password')
                serializer = UserSerializer(user_instance , data=request.data ,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    user = User.objects.get(id=request.data['id'])
                    user.set_password(request.data['password'])
                    user.save()
                    return Response({'ok': True , 'message': 'Password Changed Successful.'}, status=200)
                return Response({'ok': False , 'errors': serializer.errors}, status=400)
            return Response({'ok': False , 'messae' : 'Old password is invalid.'})
        except:
            return Response({'ok': False , 'message': 'user not exist.'},status=400)
        
    def delete(self, request, format=None):
        try:
            user_instance = User.objects.get(id=request.data['id'])
            user_instance.delete()
            return Response({'ok': True, 'messsage': 'User deleted.'}, status=200)
        except:
            return Response({'ok': True, 'message': 'User does not exist.' , 'id':request.data}, status=404)