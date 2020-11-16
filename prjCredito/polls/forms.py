from django import forms
from .models import Cadastro, Ficha


class CadastroForm(forms.ModelForm):    

    class Meta:
        model = Cadastro
        fields =  "__all__"

class FichaForm(forms.ModelForm):    

    class Meta:
        model = Ficha
        fields =  "__all__"