from django.urls import path

from . import views

namespace = 'avaliacoes'

urlpatterns = [
    path('criar/', views.avaliacao_criar, name='avaliacao_criar'),
    path('atualizar/<int:id>', views.avaliacao_atualizar, name='avaliacao_atualizar'),
    path('excluir/<int:id>', views.avaliacao_excluir, name='avaliacao_excluir'),
]