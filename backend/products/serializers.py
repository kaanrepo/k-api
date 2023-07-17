from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    my_discount = serializers.SerializerMethodField(read_only=True)
    product_edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail-view',
        lookup_field='pk'
        )

    class Meta:
        model = Product
        fields = [
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
            'product_edit_url',
            'url'
        ]

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        
        return obj.get_discount()
    
    def get_product_edit_url(self, obj):
        #return f'http://127.0.0.1:8000/api/v2/products/{obj.pk}'
        request = self.context.get('request') or None
        return reverse('product-update-view', kwargs={'pk' : obj.pk}, request=request)
