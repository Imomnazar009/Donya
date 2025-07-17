from rest_framework import serializers
from config import settings
from .models import About, AboutServices


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'title', 'description', 'image']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['title'] = getattr(instance.title, f'name_{lang}')
            data['description'] = getattr(instance, f'description_{lang}')
        return data


class GetAboutServices(serializers.ModelSerializer):
    class Meta:
        model = AboutServices
        fields = ['icon', 'name', 'description']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['name'] = getattr(instance, f'name_{lang}')
            data['description'] = getattr(instance, f'description_{lang}')
        return data



class AboutServicesSerializer(serializers.ModelSerializer):
    about_services = serializers.SerializerMethodField()

    class Meta:
        model = AboutServices
        fields = ['id', 'title', 'about_services']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['title'] = getattr(instance.title, f'name_{lang}')
        return data

    def get_about_services(self, obj):
        request = self.context.get('request')
        about_services = AboutServices.objects.all()
        return GetAboutServices(about_services, many=True, context={'request': request}).data
