from django.urls import path

from core import views as core
from mascota_api import views as mascotas

urlpatterns = [
    path('',core.index,name='index'),
    path('nuevo/',core.nuevo, name='nuevo'),
    path('formulario/', core.contacto_view, name='formulario'),

    path('mascotas/', mascotas.api_lista_mascotas, name='lista_mascotas'),
    path('mascotas/nueva/', mascotas.api_crear_mascota, name='crear_mascota'),
    path('mascotas/editar/<int:pk>/', mascotas.api_editar_mascota, name='editar_mascota'),
    path('mascotas/eliminar/<int:pk>/', mascotas.api_eliminar_mascota, name='eliminar_mascota'),

]
