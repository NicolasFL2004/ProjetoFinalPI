from django.db import models

# Create your models here.

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
    

