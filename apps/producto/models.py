from asyncio import Condition
from os import name
from django.db import models
from typing import Any


class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Producto Categoria"
        verbose_name_plural = "Productos Categorias"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField(max_length=200, null=True, blank=True)
    categoria = models.ForeignKey(ProductoCategoria, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="categoria")
    imagen = models.ImageField(upload_to="imagenes", null=True, blank=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return f"{self.nombre} (${self.precio} pesos)"
