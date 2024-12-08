from django.shortcuts import redirect, render

from .forms import JogoForm
from .models import Jogo


# Create your views here.
def index(request):
    jogos = Jogo.objects.all()
    contexto = {
        'jogos': jogos
 
    }
    return render(request, 'gameinsight/index.html', contexto)

def novo_jogo(request):
    form = JogoForm()

    if request.method == 'POST':
        form = JogoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    contexto = {
        'form': form
    }
    return render(request, 'gameinsight/avaliacao.html', contexto)

def editar_jogo(request, id):
    jogo = Jogo.objects.get(id=id)
    
    if request.method == 'POST':
        form = JogoForm(request.POST, request.FILES, instance=jogo)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = JogoForm(instance=jogo)
    
    contexto = {
        'form': form
    }
    return render(request, 'gameinsight/avaliacao.html', contexto)

def excluir_jogo(request, id):
    jogo = Jogo.objects.get(id=id)
    jogo.delete()
    return redirect('index')