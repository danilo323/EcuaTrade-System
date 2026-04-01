from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
   # name='registrar_producto' es el apodo para usarlo en el HTML después
    path('registrar/', views.registrar_producto_view, name='registrar_producto'),
]
