from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Genero, Plataforma, Jogo
# Register your models here.
class UserBlogAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('cpf', 'nome_cidade', 'nome_mae', 'endereco', 'nome_bairro')}),
    )

admin.site.register(Usuario, UserBlogAdmin)
admin.site.register(Genero)
admin.site.register(Plataforma)
admin.site.register(Jogo)
