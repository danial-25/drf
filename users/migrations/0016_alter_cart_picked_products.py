# Generated by Django 4.2.1 on 2023-06-01 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_shopping_products'),
        ('users', '0015_alter_customuser_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='picked_products',
            field=models.ManyToManyField(to='products.shopping_products'),
        ),
    ]
