from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import validate_title, validate_title_no_hello, unique_product_title
from api.serializers import UserPublicSerializer





class ProductInlineSerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):

    owner = UserPublicSerializer(source='user', read_only=True)
    #email = serializers.EmailField(source='user.email', read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True)
    product_edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail-view',
        lookup_field='pk'
        )
    
    title = serializers.CharField(validators=[validate_title])
    name = serializers.CharField(source='title', read_only=True)

    class Meta:
        model = Product
        fields = [
            'owner',
            #'email',
            'pk',
            'title', 
            'name',
            'content',
            'price',
            'sale_price',
            'my_discount',
            'product_edit_url',
            'url',
            'endpoint'
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
    
    def validate(self, data):
        print('validate test1')
        return data
    
    def validate_title(self, value):
        print('test2')
        return value
    

    
    #VALIDATION FROM HERE CAN ACCESS request data!!!
    # request = self.context.get('request')
    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f'{value} already exists.')
    #     return value
