from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("teste")


def detalhes(request):
    pass


def contratos(request):
    pass


def contrato(request, id):
    pass


def editar_perfil(request):
    pass