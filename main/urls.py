
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'main'

urlpatterns = [
    path('api/invoice', views.api_invoice, name= 'api_invoice'),
    path('api/get_all', views.api_get_all, name= 'api_get_all'),
    path('api/get_one/id=<id>', views.api_get_one, name= 'api_get_one'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
