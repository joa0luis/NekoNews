from django import forms
from .models import Noticia
from django.contrib.auth.models import User

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'conteudo','imagem']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o título'}),
            'conteudo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva o conteúdo'}),
            }

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirme sua senha'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu usuário'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu e-mail'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', 'As senhas não coincidem.')