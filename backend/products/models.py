from django.db import models
from django.conf import settings
from django.db.models import Q
from django.db.models.query import QuerySet
from rest_framework.reverse import reverse

User = settings.AUTH_USER_MODEL 

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    
    def search(self, query, user=None):
        lookups = Q(title__icontains=query) | Q(user__username__icontains=query) | Q(content__icontains=query)
        qs = self.filter(lookups).is_public()
        if user is not None:
            qs_own_data = self.filter(user=user).filter(lookups)
            qs = (qs | qs_own_data).distinct()
        return qs
    
class ProductManager(models.Manager):

    def get_queryset(self) -> QuerySet:
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, default=1, null=True)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=99.99)
    public = models.BooleanField(default=True)

    objects = ProductManager()

    @property
    def endpoint(self):
        return reverse("product-detail-view", kwargs={"pk": self.pk})
    

    def is_public(self) -> bool: 
        return self.public

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)
    
    def get_discount(self):
        return '122'