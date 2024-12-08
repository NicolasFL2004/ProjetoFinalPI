from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Usuario


class UserBlogCreationForm(UserCreationForm):
    nome_cidade = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Cidade'}))
    nome_mae = forms.CharField(max_length=100, required=False)
    endereco = forms.CharField(max_length=255, required=False)
    nome_bairro = forms.CharField(max_length=100, required=False)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar senha'}))

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2', 'nome_cidade', 'nome_mae', 'endereco', 'nome_bairro')

        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'Usuário', 'class': 'form-control'}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Email', 'class': 'form-control'}
            ), 
            'nome_cidade': forms.TextInput(),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if not hasattr(field.widget.attrs, 'class'):
                field.widget.attrs.update({'class': 'form-control'})