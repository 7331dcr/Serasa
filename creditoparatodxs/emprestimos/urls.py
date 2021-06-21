from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("detalhes", views.detalhes, name="detalhes"),
    path("contratos", views.contratos, name="contratos"),
    path("contratos/<int:id>", views.contrato, name="contrato"),
    path("editar_perfil", views.editar_perfil, name="editar_perfil"),
]
