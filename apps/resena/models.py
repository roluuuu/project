from django.db import models
from django.contrib.auth.models import User

from pedido.models import Pedido
from cliente.models import Cliente
from producto.models import Producto


class Resena(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    calificacion = models.PositiveIntegerField()
    comentario = models.TextField()

    def __str__(self):
        return f"Reseña de {self.usuario.username} para {self.producto}"
