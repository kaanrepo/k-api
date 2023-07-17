from django.urls import path

from . import views


# urlpatterns = [
#     path('', views.ProductMixinView.as_view(), name='product-list-create-view'),
#     path('<int:pk>/', views.ProductMixinView.as_view(), name='product-detail-view'),
#     path('<int:pk>/update/', views.ProductMixinView.as_view(), name='product-update-view'),
#     path('<int:pk>/delete/', views.ProductMixinView.as_view(), name='product-delete-view'),
# ]


urlpatterns = [
    # path('', views.product_alt_view, name='product-create-view'),
    # path('<int:pk>/', views.product_alt_view, name='product-detail-view'),
    path('', views.ProductListCreateAPIView.as_view(), name='product-list-create-view'),
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name='product-detail-view'),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name='product-update-view'),
    path('<int:pk>/delete/', views.ProductDestroyAPIView.as_view(), name='product-delete-view'),
]
