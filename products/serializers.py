from rest_framework import serializers
from .models import products
from rest_framework.reverse import reverse,reverse_lazy
class productsSerializer(serializers.ModelSerializer):
    # product_url=serializers.HyperlinkedIdentityField(view_name='detail', lookup_field='id')
    class Meta:
        model = products
        fields = '__all__'
    def to_representation(self, instance):
        request = self.context.get('request')
        url = reverse('products-detail', kwargs={'id': instance.id, 'category': instance.category}, request=request)
        representation = super().to_representation(instance)
        representation['url']=url
        return representation
# from rest_framework import serializers
# from .models import products
# from django.urls import reverse
# class productsSerializer(serializers.ModelSerializer):
#     url = serializers.SerializerMethodField()
#     class Meta:
#         model = products
#         fields = '__all__'

#     def get_url(self, obj):
#         # Customize this method to generate the URL based on your URL pattern and view function
#         request = self.context['request']
#         url = reverse('products-detail', kwargs={'id': obj.id})
#         return url
