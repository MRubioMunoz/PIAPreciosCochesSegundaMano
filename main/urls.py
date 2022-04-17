from django.urls import path
from . import views

urlpatterns = [
    path("", views.formulario , name="formulario"),
    path("precio/", views.precio, name="precio")

]
