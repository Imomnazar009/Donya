from django.conf import settings
from rest_framework import serializers
from .models import Footer, PhoneNumber, SocialMedia


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ['email', 'map_url']


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ['phone_number']


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ['name', 'url', 'image']
