from django.urls import path

from . import views

namespace = 'jogos'

urlpatterns = [
    path('detalhes/<int:id>/', views.jogo_detalhes, name='jogo_detalhes'),
    path('criar/', views.jogo_criar, name='jogo_criar'),
    path('atualizar/<int:id>', views.jogo_atualizar, name='jogo_atualizar'),
    path('excluir/<int:id>', views.jogo_excluir, name='jogo_excluir'),
]
