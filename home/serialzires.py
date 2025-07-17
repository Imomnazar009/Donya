from django.conf import settings
from rest_framework import serializers
from .models import Home, WhatAreWeDoing, Catalog, Sertificate, Title, Klient


class GetHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['id', 'title', 'image']


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ['id', 'title', 'image']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['title'] = getattr(instance, f'title_{lang}')
        return data

class WhatAreWeDoingSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    class Meta:
        model = WhatAreWeDoing
        fields = ['id', 'title', 'description', 'image']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['description'] = getattr(instance, f'description_{lang}')
        return data

    def get_language(self):
        request = self.context.get('request')
        lang = settings.MODELTRANSLATION_DEFAULT_LANGUAGE
        if request:
            return request.headers.get('Accept-Language', lang)
        return lang

    def get_title(self, obj):
        lang = self.get_language()
        if hasattr(obj.title, f'name_{lang}'):
            return getattr(obj.title, f'name_{lang}', obj.title.name)
        return obj.title.name


class GetSertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sertificate
        fields = ['id', 'description', 'image']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['description'] = getattr(instance, f'description_{lang}')
        return data


class GetCatalogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['id', 'description', 'image']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['description'] = getattr(instance, f'description_{lang}')
        return data


class CatalogSerializer(serializers.ModelSerializer):
    catalogs = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    class Meta:
        model = Catalog
        fields = ['id', 'title', 'catalogs']

    def get_language(self):
        request = self.context.get('request')
        lang = settings.MODELTRANSLATION_DEFAULT_LANGUAGE
        if request:
            return request.headers.get('Accept-Language', lang)
        return lang

    def get_title(self, obj):
        lang = self.get_language()
        if hasattr(obj.title, f'name_{lang}'):
            return getattr(obj.title, f'name_{lang}', obj.title.name)
        return obj.title.name

    def get_catalogs(self, obj):
        catalogs = Catalog.objects.all()
        return GetCatalogsSerializer(catalogs, many=True, context=self.context).data


class SertificateSerializer(serializers.ModelSerializer):
    certificates = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    class Meta:
        model = Sertificate
        fields = ['id', 'title', 'certificates']

    def get_certificates(self, obj):
        certificates = Sertificate.objects.all()
        return GetSertificateSerializer(certificates, many=True, context=self.context).data

    def get_language(self):
        request = self.context.get('request')
        lang = settings.MODELTRANSLATION_DEFAULT_LANGUAGE
        if request:
            return request.headers.get('Accept-Language', lang)
        return lang

    def get_title(self, obj):
        lang = self.get_language()
        if hasattr(obj.title, f'name_{lang}'):
            return getattr(obj.title, f'name_{lang}', obj.title.name)
        return obj.title.name


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ['name']


class HomeClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = ['id', 'image']


class KlientSerializer(serializers.ModelSerializer):
    klints = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    class Meta:
        model = Klient
        fields = ['id', 'title', 'klints']

    def get_language(self):
        request = self.context.get('request')
        lang = settings.MODELTRANSLATION_DEFAULT_LANGUAGE
        if request:
            return request.headers.get('Accept-Language', lang)
        return lang

    def get_title(self, obj):
        lang = self.get_language()
        if hasattr(obj.title, f'name_{lang}'):
            return getattr(obj.title, f'name_{lang}', obj.title.name)
        return obj.title.name

    def get_klints(self, obj):
        klients = Klient.objects.all()
        return HomeClientsSerializer(klients, many=True, context=self.context).data
