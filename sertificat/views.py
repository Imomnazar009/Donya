from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serialzires import SertificatSerializer
from .models import Sertificat


class SertificatViewSet(ViewSet):
    @swagger_auto_schema(
        operation_description="Barcha sertifikatlarni olish",
        operation_summary="Get all sertificats",
        responses={200: SertificatSerializer()},
        tags=["Sertificat"],
    )
    def SertificatView(self, request):
        sertificat = Sertificat.objects.first()
        if not sertificat:
            return Response({"detail": "No sertificats found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = SertificatSerializer(sertificat, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
