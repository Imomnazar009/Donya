from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from .models import About, AboutServices
from .serializers import AboutSerializer, AboutServicesSerializer
from drf_yasg.utils import swagger_auto_schema


class AboutViewSite(ViewSet):
    @swagger_auto_schema(
        responses={200: AboutSerializer(many=True)},
        operation_description="Get all About content",
        tags=['About']
    )
    def AboutView(self, request):
        about = About.objects.all().first()
        serializer = AboutSerializer(about, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class AboutServicesViewSite(ViewSet):
    @swagger_auto_schema(
        responses={200: AboutServicesSerializer(many=True)},
        operation_description="Get all About Services",
        tags=['About']
    )
    def AboutServicesView(self, request):
        services = AboutServices.objects.all().first()
        serializer = AboutServicesSerializer(services, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
