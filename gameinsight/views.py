from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Jogo
from .forms import JogoForm, UserBlogCreationForm
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('usuarios:index')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'gameinsight/login.html')

def logout_view(request):
    logout(request)
    return redirect('usuarios:login')

def register(request):
    if request.method == 'POST':
        form = UserBlogCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso! Você já pode fazer login.')
            return redirect('usuarios:login')
    else:
        form = UserBlogCreationForm()

    return render(request, 'gameinsight/register.html', {'form': form})
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