from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers
from django.contrib.auth.models import User

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...

        return token

class UserSerializer(serializers.ModelSerializer):
    # password_confirmation = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id' , 'email' , 'username' , 'password' ]

# def create(self , validate_data):
#         if validate_data['password'] != validate_data['password_confirmation']:
#             raise serializers.ValidationError('Password does not match.')
#         validate_data.pop('password_confirmation')
#         return super().create(validate_data)

def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    return user