from django.contrib.auth.models import AbstractUser
from django.db import models


class Estado(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    sigla = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} - {self.estado.sigla}'


class Usuario(AbstractUser):
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, null=True, blank=True, default=None)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, default=None)   

    def __str__(self):
        return self.username
