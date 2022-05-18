from django.shortcuts import render
from django.urls import URLPattern, path
from . import views
from django.contrib.staticfiles.urls import static
from django.conf import settings

app_name='feat'

urlpatterns = [
    path('', views.home, name='home'),
    path('feature extraction', views.extraction,name='extraction'),
    path('VBPR',views.VBPR,name="VBPR"),
    path('recomendacion',views.recomendacion, name='recomendacion'),
]+ static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)