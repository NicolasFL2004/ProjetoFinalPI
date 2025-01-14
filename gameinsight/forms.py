from django import forms

from .models import Avaliacao, Jogo


class AvaliacaoForm(forms.ModelForm):
    class Meta:
        model = Avaliacao
        fields = ('jogo', 'nota','comentario')

        widgets = {
            'jogo': forms.Select(attrs={'class': 'form-control'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control'}),
            'nota': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class JogoForm(forms.ModelForm):

    class Meta:
        model = Jogo
        fields = ('nome', 'desenvolvedora', 'genero', 'data_lancamento', 'descricao', 'plataforma', 'classificacao', 'capa')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'desenvolvedora': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'data_lancamento': forms.DateInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'plataforma': forms.Select(attrs={'class': 'form-control'}),
            'classificacao': forms.Select(attrs={'class': 'form-control'}),
            'capa': forms.FileInput(attrs={'class': 'form-control'}),
        }
