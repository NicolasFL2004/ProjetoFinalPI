from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import AvaliacaoForm
from django.db.models import Q  
from .models import Avaliacao, Jogo
from django.contrib import messages

def index(request):
    search_term = request.GET.get('q')

    if search_term:
        jogos = Jogo.objects.filter(Q(nome__icontains=search_term))
    else:
        jogos = Jogo.objects.all()

    contexto = {
        'jogos': jogos
 
    }
    return render(request, 'gameinsight/pages/index.html', contexto)


@login_required(login_url='usuarios:login')
def avaliacao_criar(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, request.FILES)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.usuario = request.user
            avaliacao.save()
            messages.success(request, 'Avaliação realizada com sucesso!')
            return redirect('index')
    
    form = AvaliacaoForm()

    contexto = {
        'form': form
    }
    return render(request, 'gameinsight/pages/avaliacao.html', contexto)


@login_required(login_url='usuarios:login')
def avaliacao_atualizar(request, id):
    avaliacao = Avaliacao.objects.get(id=id)
    
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, request.FILES, instance=avaliacao)
        if form.is_valid():
            form.save()
            messages.success(request, 'Avaliação atualizada com sucesso!')
            return redirect('index')
    else:
        form = AvaliacaoForm(instance=avaliacao)
    
    contexto = {
        'form': form
    }
    return render(request, 'gameinsight/pages/avaliacao.html', contexto)


@login_required(login_url='usuarios:login')
def avaliacao_excluir(request, id):
    avaliacao = Avaliacao.objects.get(id=id)
    avaliacao.delete()
    messages.success(request, 'Avaliação excluída com sucesso!')
    return redirect('index')
