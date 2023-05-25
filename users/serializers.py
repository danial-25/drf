from django.contrib.auth.models import User
from .models import CustomUser,cart
from rest_framework import serializers
from products.serializers import productsSerializer
class CartSerializer(serializers.ModelSerializer):
    picked_products = productsSerializer(many=True)
    class Meta:
        model = cart
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    cart = CartSerializer(allow_null=True) 
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'first_name', 'last_name', 'email','cart')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

# from .models import Profile
# from rest_framework import serializers

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ('username', 'password', 'first_name', 'last_name', 'email')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = Profile.objects.create_user(**validated_data)
#         return user