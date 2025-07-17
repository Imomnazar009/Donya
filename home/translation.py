from modeltranslation.translator import TranslationOptions, translator
from .models import Title, Catalog, Home, WhatAreWeDoing, Sertificate


class TitleTranslationOptions(TranslationOptions):
    fields = ['name']


class CatalogTranslationOptions(TranslationOptions):
    fields = ['description']


class HomeTranslationOptions(TranslationOptions):
    fields = ['title']


class WhatAreWeDoingTranslationOptions(TranslationOptions):
    fields = ['description']


class CertificateTranslationOptions(TranslationOptions):
    fields = ['description']

translator.register(Title, TitleTranslationOptions)
translator.register(Catalog, CatalogTranslationOptions)
translator.register(Home, HomeTranslationOptions)
translator.register(WhatAreWeDoing, WhatAreWeDoingTranslationOptions)
translator.register(Sertificate, CertificateTranslationOptions)
