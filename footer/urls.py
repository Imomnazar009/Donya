from django.urls import path
from .views import FooterViewSet, PhoneNumberViewSet, SocialMediaViewSet

urlpatterns = [
    path('footer/', FooterViewSet.as_view({'get': 'FooterView'}), name='footer'),
    path('phone-numbers/', PhoneNumberViewSet.as_view({'get': 'PhoneNumberView'}), name='phone-numbers'),
    path('social-media/', SocialMediaViewSet.as_view({'get': 'SocialMediaView'}), name='social-media'),
]
