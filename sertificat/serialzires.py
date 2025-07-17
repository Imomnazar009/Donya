from rest_framework import serializers
from .models import Sertificat


class GetSertificatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sertificat
        fields = ['id', 'description', 'image']


class SertificatSerializer(serializers.ModelSerializer):
    sertificats = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    class Meta:
        model = Sertificat
        fields = ['id', 'name', 'title', 'created_at', 'updated_at', 'sertificats']

    def get_name(self, obj):
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', 'uz') if request else 'uz'
        return getattr(obj, f'name_{lang}', obj.name)

    def get_title(self, obj):
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', 'uz') if request else 'uz'
        return getattr(obj, f'title_{lang}', obj.title)

    def get_sertificats(self, obj):
        queryset = Sertificat.objects.exclude(id=obj.id)  # Boshqalarni olish
        return GetSertificatSerializer(queryset, many=True, context=self.context).data
