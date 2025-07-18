"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf.urls.i18n import i18n_patterns

admin.site.site_header = 'DONYA WEB SYSTEM'
admin.site.site_title = 'DONYA WEB SYSTEM'
admin.site.index_title = 'Welcome to dashboard'

schema_view = get_schema_view(
    openapi.Info(
        title="DONYA Web System APIv1",
        default_version="v1",
        description="API for project DONYA Web System",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = i18n_patterns(
    path('api/v1/home/', include('home.urls')),
    path('api/v1/about/', include('about.urls')),
    path('api/v1/contact/', include('contact.urls')),
    path('api/v1/footer/', include('footer.urls')),
    path('api/v1/products/', include('products.urls')),
    path('api/v1/sertificat/', include('sertificat.urls')),
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui", ),
    re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
) + [path('admin/', admin.site.urls),]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += i18n_patterns(
        path('rosetta/', include('rosetta.urls'))
    )
