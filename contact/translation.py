from modeltranslation.translator import translator, TranslationOptions
from .models import Contact


class ContactTranslationOptions(TranslationOptions):
    fields = ('name', 'message')


translator.register(Contact, ContactTranslationOptions)
