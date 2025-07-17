from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactSerializer
from .models import Contact
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class ContactViewSet(ViewSet):

    @swagger_auto_schema(
        responses={200: ContactSerializer(many=True)},
        operation_description="Get all contact messages",
        tags=['Contact']
    )
    def ContactView(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
