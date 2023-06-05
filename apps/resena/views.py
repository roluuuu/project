from django.shortcuts import render
from .models import Resena

def index(request):
    resenias = Resena.objects.all()
    return render(request, 'resena/index.html', {'resenias': resenias})

