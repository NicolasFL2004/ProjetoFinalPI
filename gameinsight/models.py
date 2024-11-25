from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    nome_cidade = models.CharField(max_length=100, blank=True, null=True)
    nome_mae = models.CharField(max_length=100, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)
    nome_bairro = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.username} - {self.cpf}"


class Genero(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Plataforma(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    desenvolvedora = models.CharField(max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)
    descricao = models.TextField()
    classificacao = models.CharField(max_length=50)
    data_lancamento = models.DateField()
    comentario = models.TextField()
    nota = models.FloatField()
    capa = models.ImageField(upload_to='capas/', null=True, blank=True)

    def __str__(self):
        return self.nome
    

