from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("home.urls", "home"))),
    path("cliente/", include(("cliente.urls", "cliente"))),
    path("producto/", include(("producto.urls", "producto"))),
    path("resena/", include(("resena.urls", "resena"))),
    path("pedido/", include(("pedido.urls", "pedido"))),
]
