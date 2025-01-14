from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from gameinsight.forms import JogoForm
from rolepermissions.decorators import has_role_decorator
from gameinsight.models import Jogo, Avaliacao
from django.contrib import messages
from django.db.models import Case, When, Value, IntegerField



@login_required(login_url='usuarios:login')
def jogo_detalhes(request, id):
    jogo = Jogo.objects.get(id=id)
    contexto = {
        'jogo': jogo
    }

    avaliacoes = Avaliacao.objects.filter(jogo=jogo).annotate(
        prioridade=Case(
            When(usuario=request.user, then=Value(1)),
            default=Value(2),
            output_field=IntegerField(),
        )
    ).order_by('prioridade', '-id')

    contexto['avaliacoes'] = avaliacoes

    return render(request, 'gameinsight/pages/jogo_detalhes.html', contexto)


login_required(login_url='usuarios:login')
@has_role_decorator("Admin")
def jogo_criar(request):
    if request.method == 'POST':
        form = JogoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Jogo criado com sucesso!')
            return redirect('index')
    
    form = JogoForm()

    contexto = {
        'form': form
    }
    return render(request, 'gameinsight/pages/jogo_form.html', contexto)


@login_required(login_url='usuarios:login')
@has_role_decorator("Admin")
def jogo_atualizar(request, id):
    jogo = Jogo.objects.get(id=id)
    
    if request.method == 'POST':
        form = JogoForm(request.POST, request.FILES, instance=jogo)
        if form.is_valid():
            jogo_form = form.save(commit=False)
            if 'capa' not in request.FILES:
                jogo_form.capa = jogo.capa
            jogo_form.save()
            messages.success(request, 'Jogo atualizado com sucesso!')
            return redirect('index')
    else:
        form = JogoForm(instance=jogo)
    
    contexto = {
        'form': form
    }
    return render(request, 'gameinsight/pages/jogo_form.html', contexto)


@login_required(login_url='usuarios:login')
@has_role_decorator("Admin")
def jogo_excluir(request, id):
    jogo = Jogo.objects.get(id=id)
    jogo.delete()
    messages.success(request, 'Jogo excluído com sucesso!')
    return redirect('index')
