from rest_framework import serializers
from .models import products
class productsSerializer(serializers.ModelSerializer):
    product_url=serializers.HyperlinkedIdentityField(
        view_name='products-detail', lookup_field='id'
    )
    class Meta:
        model = products
        fields = '__all__'
