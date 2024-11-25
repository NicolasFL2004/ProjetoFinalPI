from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Jogo, Usuario

class UserBlogCreationForm(UserCreationForm):
    cpf = forms.CharField(max_length=11, required=True, help_text="Digite seu CPF sem pontos ou traços.")
    nome_cidade = forms.CharField(max_length=100, required=False)
    nome_mae = forms.CharField(max_length=100, required=False)
    endereco = forms.CharField(max_length=255, required=False)
    nome_bairro = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Usuario
        fields = ('username', 'cpf', 'email', 'password1', 'password2', 'nome_cidade', 'nome_mae', 'endereco', 'nome_bairro')


class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'desenvolvedora': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'plataforma': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'classificacao': forms.TextInput(attrs={'class': 'form-control'}),
            'data_lancamento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control'}),
            'nota': forms.NumberInput(attrs={'class': 'form-control'}),
            'capa': forms.FileInput(attrs={'class': 'form-control'}),
        }