from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg
from usuarios.models import Usuario 
from django.core.exceptions import ValidationError


class Genero(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Plataforma(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Classificacao(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    desenvolvedora = models.CharField(max_length=100)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    data_lancamento = models.DateField()
    descricao = models.TextField()
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)
    classificacao = models.ForeignKey(Classificacao, on_delete=models.CASCADE)
    capa = models.ImageField(upload_to='capas/', null=True, blank=True)
    media = models.FloatField(default=0.0)


    def __str__(self):
        return self.nome
    
    def atualizar_media(self):
        self.media = self.avaliacoes.aggregate(Avg('nota'))['nota__avg'] or 0.0
        self.save()

class Avaliacao(models.Model):
    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE, related_name='avaliacoes')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    nota = models.FloatField(validators=[
        MinValueValidator(0.0),
        MaxValueValidator(5.0)
    ])
    comentario = models.TextField()

    def __str__(self):
        return f"Jogo: {self.jogo.nome} - Avaliação de: {self.usuario.username}"
