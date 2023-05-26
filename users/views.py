from django.shortcuts import render

# Create your views here.
import re
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import permissions
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import cart,CustomUser
from django.contrib.auth.models import User
from products.models import products
from products.serializers import productsSerializer


class UserRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully.'}, status=201)
        return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)
    if user:
        token,_= Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=200)
    return Response({'error': 'Invalid credentials'}, status=401)

class DataAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        if request.auth:
            
            User=get_user_model()
            user = User.objects.get(id=request.user.id)
            serializer = UserSerializer(user)
            serialized_data = serializer.data


            name=serialized_data['first_name']
            lastname=serialized_data['last_name']
            cart=serialized_data['cart']
        return Response({'name': name, 'lastname':lastname, 'cart':cart})


@api_view(['POST'])
@permission_classes([AllowAny])
@authentication_classes([TokenAuthentication])
def add_item(request):
    quantity = request.data.get('quantity')
    product_id = request.data.get('pid')
    
    User = get_user_model()
    user = User.objects.get(id=request.user.id)
    
    if user.cart:
        obj=user.cart
    else:
        obj = cart()
        obj.save()
        user.cart = obj  # Assign the cart object directly to the user's cart field
        user.save()
    if(user.cart.picked_products.filter(id=product_id).exists()==False):
        obj.picked_products.add(products.objects.get(id=product_id))
    obj.quantity += int(quantity)
    obj.save()
    

    
    # Calculate the total price
    picked_products = obj.picked_products.get(id=product_id)
    total_price = 0
    # for product in picked_products:
    value_without_comma = picked_products.price.replace(',', '') 
    value_without_comma = value_without_comma.replace('.00', '')
    numeric_value = ''.join(filter(str.isdigit, value_without_comma))  
    price = int(numeric_value) 
    total_price += price

    obj.total_price += total_price
    obj.save()

    return Response(status=200)



# def add_item(request):
#     quantity=request.data.get('quantity')
#     product_id=request.data.get('pid')
    
#     User=get_user_model()
#     user = User.objects.get(id=request.user.id)
#     user.cart.add(cart())
#     user.cart.save()
#     product = products.objects.get(id=product_id)
#     user.cart.picked_products.set([product])#it creates new value, and it should add up to already existing value, also it shouldn't create new object if id is same
#     user.cart.quantity+=int(quantity)#it creates new value, and it should add up to already existing value
#     user.cart.save()
#     user.save()
#     use=UserSerializer(user)
#     value_without_comma = product.price.replace(',', '') 
#     value_without_comma = value_without_comma.replace('.00', '')
#     numeric_value = ''.join(filter(str.isdigit, value_without_comma))  
#     price = int(numeric_value) 
#     total_price = user.cart.total_price + (price * int(quantity))
#     user.cart.total_price = total_price
    
#     user.cart.save()  # Save the cart object
#     user.save()  # Save the user object
    
#     use = UserSerializer(user)
#     serialized_data = use.data
    
#     return Response(serialized_data, status=200)
# from django.shortcuts import render
# from rest_framework.permissions import AllowAny
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .serializers import UserSerializer
# from django.contrib.auth.models import User
# from rest_framework.authentication import TokenAuthentication
# from rest_framework import generics
# from rest_framework.authtoken.models import Token
# from django.contrib.auth import authenticate
# from rest_framework import permissions
# from rest_framework.decorators import api_view,permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.views import APIView
# from rest_framework.response import Response

# class UserRegistrationView(generics.CreateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class=UserSerializer
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'User registered successfully.'}, status=201)
#         return Response(serializer.errors, status=400)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def user_login(request):
#     username = request.data.get('User').get('username')
#     password = request.data.get('User').get('password')

#     user = authenticate(request, username=username, password=password)
#     if user:
#         token,_= Token.objects.get_or_create(user=user)
#         return Response({'token': token.key}, status=200)
#     return Response({'error': 'Invalid credentials'}, status=401)

# class DataAPIView(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request):
#         if request.auth:
#             name=request.user.first_name
#             lastname=request.user.last_name
#             cart=request.user.cart
#         return Response({'name': name, 'lastname':lastname, 'cart':cart})
