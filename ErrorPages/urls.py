from django.urls import path

from core import views as core

urlpatterns = [
    path('',core.index,name='index'),
    path('nuevo/',core.nuevo, name='nuevo'),
]
