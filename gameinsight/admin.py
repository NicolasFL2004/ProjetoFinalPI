from django.contrib import admin
from .models import Usuario, Genero, Plataforma, Jogo, Destaque
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Genero)
admin.site.register(Plataforma)
admin.site.register(Jogo)
admin.site.register(Destaque)