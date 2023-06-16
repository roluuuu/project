from django import forms
from . import models


class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = "__all__"


class ProductoCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.ProductoCategoria
        fields = "__all__"
