from django.urls import path, register_converter
from . import views

urlpatterns = [
    path('<str:namepage>', views.index, name='index'),
]
