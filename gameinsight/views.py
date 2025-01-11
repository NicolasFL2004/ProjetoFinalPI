from django.shortcuts import redirect, render

from .forms import AvaliacaoForm
from .models import Avaliacao, Jogo


# Create your views here.
def index(request):
    jogos = Jogo.objects.all()
    contexto = {
        'jogos': jogos
 
    }
    return render(request, 'gameinsight/pages/index.html', contexto)

def avaliacao_criar(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, request.FILES)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.usuario = request.user
            avaliacao.save()
            return redirect('index')
    
    form = AvaliacaoForm()

    contexto = {
        'form': form
    }
    return render(request, 'gameinsight/pages/avaliacao.html', contexto)

def avaliacao_atualizar(request, id):
    avaliacao = Avaliacao.objects.get(id=id)
    
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, request.FILES, instance=avaliacao)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AvaliacaoForm(instance=avaliacao)
    
    contexto = {
        'form': form
    }
    return render(request, 'gameinsight/pages/avaliacao.html', contexto)

def avaliacao_excluir(request, id):
    avaliacao = Avaliacao.objects.get(id=id)
    avaliacao.delete()
    return redirect('index')
