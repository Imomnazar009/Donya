from modeltranslation.translator import TranslationOptions, translator
from .models import About, AboutServices


class AboutTranslationOptions(TranslationOptions):
    fields = ['description']


class AboutServicesTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


translator.register(About, AboutTranslationOptions)
translator.register(AboutServices, AboutServicesTranslationOptions)