from django import forms
from .models import Cadastro, Ficha
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CadastroForm(forms.ModelForm):    

    class Meta:
        model = Cadastro
        fields =  "__all__"

class FichaForm(forms.ModelForm):    

    class Meta:
        model = Ficha
        fields =  "__all__"

class OperadorForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", 'email')

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está cadastrado. Tente novamente!")
        return email