from django.urls import path
from .views import AboutViewSite, AboutServicesViewSite

urlpatterns = [
    path('about/', AboutViewSite.as_view({'get': 'AboutView'}), name='about'),
    path('about/services/', AboutServicesViewSite.as_view({'get': 'AboutServicesView'}), name='about-services'),
]
