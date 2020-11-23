from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from . models import Ficha, Cadastro, Cargo
from django.contrib import messages
from .forms import CadastroForm, FichaForm, OperadorForm, CargoForm
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import Group, User
from django.shortcuts import (get_object_or_404, 
                              render,  
                              HttpResponseRedirect) 
from django.http import HttpResponse
# Create your views here.

class Dashboard(ListView):
    model = Ficha
    template_name = 'polls/dashboard.html'


class CadastroFicha(CreateView):
    model = Cadastro
    template_name = 'polls/cadastro_perfil.html'
    fields = ["id_cargo", "nome", "rg", "cpf", "cep", "renda", "qtd_filhos", "estado_civil", "tempo_cargo"]
    success_url = "/polls/solicitar_ficha"

    def form_valid(self, form):
        form.instance.id_cliente = self.request.user
        return super().form_valid(form)

"""class SolicitarFicha(CreateView):
    model = Ficha
    template_name = 'polls/solicitar_ficha.html'
    fields = "__all__"
    success_url = "/"""

def solicitar_ficha(request):
    if request.method == 'POST':
        form = FichaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = FichaForm()
    return render(request, 'polls/solicitar_ficha.html', {'form': form})

class FichaDetalhe(DetailView):
    model = Ficha
    template_name = "polls/detalhes_ficha.html"
    fields = "__all__"

class CadastroCargo(CreateView):
    model = Cargo
    template_name = 'polls/cadastrar_cargo.html'
    fields = "__all__"
    success_url = "."  

class ListarCargos(ListView):
    model = Cargo
    template_name = 'polls/lista_cargos.html'

def excluir_cargo(request, id_cargo): 
    cargo = Cargo.objects.get(id=id_cargo) 
    cargo.delete() 

    return HttpResponseRedirect("/polls/listar_cargos") 

def atualizar_cargo(request, id_cargo): 
    context = {}

    cargo = Cargo.objects.get(id=id_cargo) 
  
    form = CargoForm(request.POST or None, instance = cargo) 
  
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/polls/listar_cargos") 
   
    context["form"] = form 
  
    return render(request, "polls/atualizar_cargo.html", context) 

class EsteiraOperador(ListView):
    model = Ficha
    template_name = 'polls/esteira_analise.html'

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

def atribuirOperador(request, id_ficha):
    ficha = Ficha.objects.get(id=id_ficha)

    ficha.status = 'E'
    ficha.id_operador = request.user
    ficha.save()

    return HttpResponseRedirect("/detalhes_ficha/" + id_ficha) 

class ListarOperadores(ListView):
    model = User
    template_name = 'polls/listar_operadores.html'

    def get_queryset(self):
        return self.model.objects.filter(groups = Group.objects.get(name='Operador'))

def excluir_operador(request, id_operador): 
    operador = User.objects.get(id=id_operador) 
    operador.delete() 

    return HttpResponseRedirect("/polls/listar_operadores") 

def atualizar_operador(request, id_operador): 
    context = {}

    operador = User.objects.get(id=id_operador) 
  
    form = OperadorForm(request.POST or None, instance = operador) 
  
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/polls/listar_operadores") 
   
    context["form"] = form 
  
    return render(request, "polls/atualizar_operador.html", context) 

def verificar_cadastro(request):
    context = {}
 
    try: 
        Cadastro.objects.get(id_cliente=request.user.id)
        return HttpResponseRedirect("/polls/solicitar_ficha") 
    except:
        return HttpResponseRedirect("/polls/cadastro_perfil")  

  