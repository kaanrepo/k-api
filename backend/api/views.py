from django.forms.models import model_to_dict
#from django.http import JsonResponse, HttpResponse

from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


# @api_view(['GET'])
# def api_home(request, *args, **kwargs):
#     """
#     DRF API VIEW
#     """
#     instance = Products.objects.all().order_by('?').first()
#     data = {}
#     if instance:
#         # data = model_to_dict(model_data, fields=['id','content'])
#         data = ProductSerializer(instance).data
#     return Response(data)

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(instance)
        return Response(serializer.data)
