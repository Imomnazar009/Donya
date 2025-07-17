from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .serialzires import HomeSerializer, WhatAreWeDoingSerializer, CatalogSerializer, SertificateSerializer, \
    TitleSerializer, KlientSerializer
from .models import Home, WhatAreWeDoing, Catalog, Sertificate, Title, Klient


class HomeViewSet(ViewSet):
    @swagger_auto_schema(responses={200: HomeSerializer()}, tags=["Home"])
    def HomeView(self, request):
        instance = Home.objects.all().first()
        serializer = HomeSerializer(instance, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class WhatAreWeDoingViewSet(ViewSet):
    @swagger_auto_schema(responses={200: WhatAreWeDoingSerializer()}, tags=["WhatAreWeDoing"])
    def WhatAreWeDoingView(self, request):
        instance = WhatAreWeDoing.objects.all().first()
        serializer = WhatAreWeDoingSerializer(instance, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CatalogViewSet(ViewSet):
    @swagger_auto_schema(responses={200: CatalogSerializer(many=True)}, tags=["Catalog"])
    def CatalogView(self, request):
        queryset = Catalog.objects.all().first()
        serializer = CatalogSerializer(queryset, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class SertificateViewSet(ViewSet):
    @swagger_auto_schema(responses={200: SertificateSerializer()}, tags=["Sertificate"])
    def SertificateView(self, request):
        instance = Sertificate.objects.all().first()
        serializer = SertificateSerializer(instance, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class TitleViewSet(ViewSet):
    @swagger_auto_schema(responses={200: TitleSerializer(many=True)}, tags=["Title"])
    def TitleView(self, request):
        queryset = Title.objects.all()
        serializer = TitleSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class KlientViewSet(ViewSet):
    @swagger_auto_schema(responses={200: KlientSerializer()}, tags=["Klient"])
    def KlientView(self, request):
        instance = Klient.objects.all().first()
        serializer = KlientSerializer(instance, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
