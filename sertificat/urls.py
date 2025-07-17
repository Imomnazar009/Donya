from django.urls import path
from .views import SertificatViewSet

urlpatterns = [
    path('sertificat/', SertificatViewSet.as_view({'get': 'SertificatView'}), name='sertificat-list'),
]
