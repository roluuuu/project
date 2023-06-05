from django.urls import path
from . import views

urlpatterns = [
    path("resena", views.index, name="index"),]