from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "producto"

urlpatterns = [
    path("", views.index, name="index"),
    path("producto_lista/", views.ProductoLista.as_view(), name="producto_lista"),
    path("producto_create/", views.ProductoCreate.as_view(), name="producto_create"),
    path("producto_delete/<int:pk>/", views.ProductoDeleteView.as_view(), name="producto_delete"),
    path("producto_update/<int:pk>/", views.ProductoUpdate.as_view(), name="producto_update"),
    path("producto_detail/<int:pk>/", views.ProductoDetail.as_view(), name="producto_detail"),
    path("productocategoria_lista/", views.ProductoCategoriaLista.as_view(), name="productocategoria_lista"),
    path("productocategoria_create/", views.ProductoCategoriaCreate.as_view(), name="productocategoria_create"),
    path("productocategoria_delete/<int:pk>/", views.ProductoCategoriaDeleteView.as_view(), name="productocategoria_delete"),
    path("productocategoria_update/<int:pk>/", views.ProductoCategoriaUpdate.as_view(), name="productocategoria_update"),
    path("productocategoria_detail/<int:pk>/", views.ProductoCategoriaDetail.as_view(), name="productocategoria_detail"),
]
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
