from django.urls import path
from .views import UserRegistrationView, user_login,DataAPIView,add_item

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', user_login, name='user-login'),
    path('data/', DataAPIView.as_view()),
    path('add_item/', add_item),
]