from django.conf import settings
from rest_framework import serializers
from .models import Product
from home.models import Catalog  # Agar Catalog boshqa appda bo‘lsa


class ProductCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['id', 'description']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['description'] = getattr(instance, f'description_{lang}')
        return data


class AboutCatalogSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    product_catalogs = serializers.SerializerMethodField()

    class Meta:
        model = Catalog
        fields = ['title', 'product_catalogs']

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

    def get_product_catalogs(self, obj):
        request = self.context.get('request')
        catalogs = Catalog.objects.all()
        return ProductCatalogSerializer(catalogs, many=True, context={'request': request}).data


class GetProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['id', 'description']


class AboutProductSerializer(serializers.ModelSerializer):
    catalog = GetProductSerializer()

    class Meta:
        model = Product
        fields = ['id', 'catalog', 'name', 'image']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES
        if lang in lang_options:
            data['name'] = getattr(instance, f'name_{lang}')
        return data

