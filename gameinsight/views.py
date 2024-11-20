from django.shortcuts import render, redirect
from .models import Jogo, Destaque
from .forms import JogoForm
# Create your views here.
def index(request):
    jogos = Jogo.objects.all()
    jogo_destaque = Destaque.objects.all()
    contexto = {
        'jogos': jogos,
        'jogo_destaque': jogo_destaque
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
    return render(request, 'gameinsight/novo_jogo.html', contexto)

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
    return render(request, 'gameinsight/novo_jogo.html', contexto)

def excluir_jogo(request, id):
    jogo = Jogo.objects.get(id=id)
    jogo.delete()
    return redirect('index')