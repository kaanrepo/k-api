from rest_framework import generics

from products.models import Product
from products.serializers import ProductSerializer


class SearchListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q') or None
        if q is None:
            return Product.objects.none()
        user = self.request.user or None
        results = qs.search(q, user=user)
        return results


