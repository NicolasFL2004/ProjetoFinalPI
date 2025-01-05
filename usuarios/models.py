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
    nome_mae = models.CharField(max_length=100, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    nome_bairro = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
