from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Producto

def index(request: HttpRequest) -> HttpResponse:
    productos = Producto.objects.all()
    return render(request, 'producto/index.html', {'productos': productos})


