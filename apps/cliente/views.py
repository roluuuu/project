from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Cliente


def index(request: HttpRequest) -> HttpResponse:
    clientes = Cliente.objects.all()
    return render(request, "cliente/index.html", {"clientes": clientes})
