from rest_framework import serializers
from .models import Contact
from config import settings


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'message']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.headers.get('Accept-Language', settings.MODELTRANSLATION_DEFAULT_LANGUAGE)
        lang_options = settings.MODELTRANSLATION_LANGUAGES

        if lang in lang_options:
            name_field = f'name_{lang}'
            message_field = f'message_{lang}'
            data['name'] = getattr(instance, name_field, instance.name)
            data['message'] = getattr(instance, message_field, instance.message)

        return data