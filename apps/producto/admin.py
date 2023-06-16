from django.contrib import admin
from .models import Producto
from .models import ProductoCategoria

# admin.site.register(Producto)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "precio",
        "descripcion",
        "categoria",
    )
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre",)
    #  list_display_links = ()
    # list_filter = ()
    # list_select_related = False
    # list_per_page = 100
    # list_max_show_all = 200
    # list_editable = ()


@admin.register(ProductoCategoria)
class ProductoCategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre",)
