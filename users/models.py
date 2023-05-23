# from django.db import models
# from django.contrib.postgres.fields import ArrayField
# from products.models import products
# from django.contrib.auth.models import User
# class cart(models.Model):
#     picked_products=models.ManyToManyField(products)
#     total_price=models.BigIntegerField()

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     cart=models.ForeignKey(cart, on_delete=models.CASCADE)