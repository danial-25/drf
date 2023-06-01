from django.db import models
from products.models import products, shopping_products
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
class cart(models.Model):
    picked_products=models.ManyToManyField(products)
    # picked_products=models.ManyToManyField(shopping_products)
    total_price=models.BigIntegerField(default=0)
    quantity=models.IntegerField(default=0)

class CustomUser(AbstractUser):
    cart=models.OneToOneField(cart, on_delete=models.SET_DEFAULT, null=True, blank=True,default=None)
