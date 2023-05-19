from django.db import models


class products(models.Model):
    title=models.CharField(max_length=256)
    price=models.CharField(max_length=256)
    shop=models.CharField(max_length=256)
    category=models.CharField(max_length=256)
    pid=models.CharField(max_length=256)
    image=models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title
