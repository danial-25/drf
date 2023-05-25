from django.db import models
from products.models import products
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
class cart(models.Model):
    picked_products=models.ManyToManyField(products)
    total_price=models.BigIntegerField(default=0)
    quantity=models.IntegerField(default=0)

class CustomUser(AbstractUser):
    cart=models.ForeignKey(cart, on_delete=models.CASCADE, null=True, blank=True)
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     cart=models.ForeignKey(cart, on_delete=models.CASCADE)