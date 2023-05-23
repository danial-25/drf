from django.shortcuts import render

# Create your views here.
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
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

class UserRegistrationView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully.'}, status=201)
        return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
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
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if request.auth:
            name=request.user.first_name
            lastname=request.user.last_name
        return Response({'name': name, 'lastname':lastname})
    




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
