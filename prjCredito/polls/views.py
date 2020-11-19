from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from . models import Ficha, Cadastro, Cargo
from django.contrib import messages
from .forms import CadastroForm, FichaForm, OperadorForm
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import Group
from django.http import HttpResponse
# Create your views here.

class Dashboard(ListView):
    model = Ficha
    template_name = 'polls/dashboard.html'


class CadastroFicha(CreateView):
    model = Cadastro
    template_name = 'polls/cadastro_perfil.html'
    fields = "__all__"
    success_url = "/"

class CadastroCargo(CreateView):
    model = Cargo
    template_name = 'polls/cadastrar_cargo.html'
    fields = "__all__"
    success_url = "."  

def CadastroOperador(request):
    if request.method == 'POST':
        form = OperadorForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            user.groups.add(Group.objects.get(name='Operador'))
            return HttpResponse('Operador cadastrado')
    else:
        form = OperadorForm()
    return render(request, 'polls/cadastrar_operador.html', {'form': form})
  