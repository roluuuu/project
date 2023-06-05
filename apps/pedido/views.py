from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Pedido

def index(request: HttpRequest) -> HttpResponse:
    pedidos = Pedido.objects.all()
    return render(request, 'pedido/index.html', {'pedidos': pedidos})
