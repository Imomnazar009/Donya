from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serialziers import FooterSerializer, PhoneNumberSerializer, SocialMediaSerializer
from .models import Footer, PhoneNumber, SocialMedia


class FooterViewSet(ViewSet):
    @swagger_auto_schema(
        responses={200: FooterSerializer()},
        operation_description="Get footer information",
        tags=['Footer']
    )
    def FooterView(self, request):  # <-- DRF standarti: 'list' ishlatiladi
        footer = Footer.objects.first()
        if footer:
            serializer = FooterSerializer(footer, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "No footer data found."}, status=status.HTTP_404_NOT_FOUND)


class PhoneNumberViewSet(ViewSet):
    @swagger_auto_schema(
        responses={200: PhoneNumberSerializer(many=True)},
        operation_description="Get phone numbers",
        tags=['PhoneNumber']
    )
    def PhoneNumberView(self, request):  # <-- to'g'ri nom: 'list'
        phone_numbers = PhoneNumber.objects.all()
        serializer = PhoneNumberSerializer(phone_numbers, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class SocialMediaViewSet(ViewSet):
    @swagger_auto_schema(
        responses={200: SocialMediaSerializer(many=True)},
        operation_description="Get social media links",
        tags=['SocialMedia']
    )
    def SocialMediaView(self, request):  # <-- to'g'ri nom: 'list'
        social_media = SocialMedia.objects.all()
        serializer = SocialMediaSerializer(social_media, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
