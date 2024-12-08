from django.urls import path

from . import views

namespace = 'jogos'

urlpatterns = [
    path('jogo/novo', views.novo_jogo, name='novo_jogo'),
    path('jogo/editar/<int:id>', views.editar_jogo, name='editar_jogo'),
    path('jogo/excluir/<int:id>', views.excluir_jogo, name='excluir_jogo'),
]