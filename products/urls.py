from django.urls import path
from .views import ProductViewSet, ProductCatalogListViewSet

urlpatterns = [
    path('products/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'}), name='product-list'),
    path('catalogs/', ProductCatalogListViewSet.as_view({'get': 'list'}), name='catalogs-list'),
]
