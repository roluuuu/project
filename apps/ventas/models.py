from django.db import models
from django.contrib.auth.models import User


class Vendedor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)

    class Meta:
        verbose_name = "Vendedor"
        verbose_name_plural = "Vendedores"

    def __str__(self):
        return f"{self.user.username}"
