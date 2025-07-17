from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serialziers import AboutProductSerializer, AboutCatalogSerializer
from .models import Product
from home.models import Catalog


class ProductViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Get products by catalog ID",
        responses={200: AboutProductSerializer(many=True)},
        tags=["Products"]
    )
    def retrieve(self, request, pk=None):  # `pk` bu yerda katalog ID
        catalog = Catalog.objects.filter(id=pk).first()
        if not catalog:
            return Response({'error': 'Catalog not found'}, status=status.HTTP_404_NOT_FOUND)
        products = Product.objects.filter(catalog=catalog)
        serializer = AboutProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductCatalogListViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Get all catalogs",
        responses={200: AboutCatalogSerializer(many=True)},
        tags=["Catalogs"]
    )
    def list(self, request):
        catalogs = Catalog.objects.all().first()
        serializer = AboutCatalogSerializer(catalogs, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
