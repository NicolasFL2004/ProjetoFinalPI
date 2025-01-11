from django.contrib import admin
from .models import Genero, Plataforma, Jogo, Avaliacao, Classificacao

admin.site.register(Genero)
admin.site.register(Plataforma)
admin.site.register(Classificacao)


@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):  
    list_display = ('nome', 'desenvolvedora', 'genero', 'plataforma', 'classificacao', 'data_lancamento', 'media')
    list_filter = ('genero', 'plataforma', 'classificacao')

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ('jogo', 'usuario', 'nota', 'comentario')
    list_filter = ('jogo', 'nota')
