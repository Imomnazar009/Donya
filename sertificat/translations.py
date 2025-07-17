from modeltranslation.translator import translator, TranslationOptions
from .models import Sertificat


class SertificatTranslationOptions(TranslationOptions):
    fields = ('name', 'title')


translator.register(Sertificat, SertificatTranslationOptions)
