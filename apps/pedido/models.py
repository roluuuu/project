from django.db import models
from django.utils import timezone

class Pedido(models.Model):
    cliente = models.ForeignKey('cliente.Cliente', on_delete=models.CASCADE)
    producto = models.ForeignKey('producto.Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_pedido = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.cliente} - {self.producto}"

