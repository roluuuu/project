from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from . import models, forms
from django.template import context
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ProductoCategoriaForm, ProductoForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def index(request: HttpRequest) -> HttpResponse:
    # productos = Producto.objects.all()
    return render(
        request,
        "producto/index.html",
    )


# ******PRODUCTO****
class ProductoLista(ListView):
    model = models.Producto

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Producto.objects.filter(nombre__icontains=query)
        else:
            object_list = models.Producto.objects.all()
        return object_list

    template_name = "producto/producto_lista.html"
    # context_object_name = 'categorias'


class ProductoCreate(LoginRequiredMixin, CreateView):
    model = models.Producto
    template_name = "producto/producto_create.html"
    form_class = ProductoForm
    success_url = reverse_lazy("producto:index")


class ProductoDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Producto
    template_name = "producto/producto_delete.html"
    success_url = reverse_lazy("producto:producto_lista")


class ProductoUpdate(LoginRequiredMixin, UpdateView):
    model = models.Producto
    template_name = "producto/producto_update.html"
    form_class = ProductoForm
    success_url = reverse_lazy("producto:index")


class ProductoDetail(DetailView):
    model = models.Producto
    template_name = "producto/producto_detail.html"


# ******PRODUCTOCATEGORIA****
class ProductoCategoriaLista(ListView):
    model = models.ProductoCategoria

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.ProductoCategoria.objects.filter(nombre__icontains=query)
        else:
            object_list = models.ProductoCategoria.objects.all()
        return object_list

    template_name = "producto/productocategoria_lista.html"


class ProductoCategoriaCreate(LoginRequiredMixin, CreateView):
    model = models.ProductoCategoria
    template_name = "producto/productocategoria_create.html"
    form_class = ProductoCategoriaForm
    success_url = reverse_lazy("producto:index")


class ProductoCategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = models.ProductoCategoria
    template_name = "producto/productocategoria_delete.html"
    success_url = reverse_lazy("producto:producto_lista")


class ProductoCategoriaUpdate(LoginRequiredMixin, UpdateView):
    model = models.ProductoCategoria
    template_name = "producto/productocategoria_update.html"
    form_class = ProductoCategoriaForm
    success_url = reverse_lazy("producto:index")


class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria
    template_name = "producto/productocategoria_detail.html"
