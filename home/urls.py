from django.urls import path
from .views import (
    HomeViewSet, WhatAreWeDoingViewSet, CatalogViewSet,
    SertificateViewSet, TitleViewSet, KlientViewSet
)

urlpatterns = [
    path('home/', HomeViewSet.as_view({'get': 'HomeView'}), name='home'),
    path('what-are-we-doing/', WhatAreWeDoingViewSet.as_view({'get': 'WhatAreWeDoingView'}), name='what_are_we_doing'),
    path('catalog/', CatalogViewSet.as_view({'get': 'CatalogView'}), name='catalog'),
    path('sertificate/', SertificateViewSet.as_view({'get': 'SertificateView'}), name='sertificate'),
    path('title/', TitleViewSet.as_view({'get': 'TitleView'}), name='title'),
    path('klient/', KlientViewSet.as_view({'get': 'KlientView'}), name='klient'),
]
