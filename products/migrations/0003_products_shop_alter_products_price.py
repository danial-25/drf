# Generated by Django 4.1.4 on 2023-05-13 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='shop',
            field=models.CharField(default=0, max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.CharField(max_length=256),
        ),
    ]
