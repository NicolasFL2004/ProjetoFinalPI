from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Usuario


class UserBlogCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if not hasattr(field.widget.attrs, 'class'):
                field.widget.attrs.update({'class': 'form-control'})


    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar senha'}))

    class Meta:
        model = Usuario
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'cidade')

        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'Nome'}
            ),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Sobrenome'}
            ),
            'username': forms.TextInput(
                attrs={'placeholder': 'Usuário'}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Email'}
            ), 
            'cidade': forms.Select(),
        }
    