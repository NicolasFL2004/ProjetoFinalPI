from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from gameinsight.models import Avaliacao
from .forms import UserBlogCreationForm, UserBlogEditForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'usuarios/login.html')


@login_required(login_url='usuarios:login')
def logout_view(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso!')
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
    print(form.errors)
    return render(request, 'usuarios/register.html', {'form': form})


@login_required(login_url='usuarios:login')
def perfil(request):
    avaliacao = Avaliacao.objects.filter(usuario=request.user).last()

    contexto = {
        'avaliacao': avaliacao
    }
    return render(request, 'usuarios/perfil.html', contexto)


@login_required(login_url='usuarios:login')
def perfil_edit(request):
    user = request.user
    if request.method == 'POST':
        form = UserBlogEditForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            print(form.cleaned_data)
            user = form.save(commit=False)
            if form.cleaned_data.get("password1"):
                user.set_password(form.cleaned_data["password1"])
            user.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('usuarios:perfil')
    else:
        form = UserBlogEditForm(instance=user)

    return render(request, 'usuarios/perfil-edit.html', {'form': form})
