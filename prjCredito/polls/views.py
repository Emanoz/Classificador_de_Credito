from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, UpdateView
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
            ficha = form.save(commit=False)
            cadastro = Cadastro.objects.get(id_cliente=request.user)
            cargo = Cargo.objects.get(id=cadastro.id_cargo.id)
            minimo_cargo = cargo.salario_minimo
            maximo_cargo = cargo.salario_maximo

            ficha.id_cadastro = cadastro

            if validar_cpf(cadastro.cpf) == 0:
                ficha.status = 'R'
                ficha.motivo_recusa = 'O CPF é inválido'
                ficha.save()
                return HttpResponseRedirect("/") 
            elif cadastro.idade < 18:
                ficha.status = 'R'
                ficha.motivo_recusa = 'O cliente é menor de idade'
                ficha.save()
                return HttpResponseRedirect("/")
            elif cadastro.renda <= minimo_cargo or cadastro.renda >= maximo_cargo:
                ficha.status = 'R'
                ficha.motivo_recusa = 'A renda não é compatível com o cargo - risco de fraude'
                ficha.save()
                return HttpResponseRedirect("/")
            elif calcular_risco(cadastro) > 10:
                ficha.status = 'R'
                ficha.motivo_recusa = 'O risco para a liberação de crédito é muito alta'
                ficha.save()
                return HttpResponseRedirect("/")
            else:   
                ficha.status = 'A'
                ficha.save()
                return HttpResponseRedirect("/")
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

    return HttpResponseRedirect("/polls/" + id_ficha) 

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
        Cadastro.objects.get(id_cliente=request.user)
        return HttpResponseRedirect("/polls/solicitar_ficha") 
    except Cadastro.DoesNotExist:
        return HttpResponseRedirect("/polls/cadastro_perfil") 

def atualizar_perfil(request, id_user): 
    context = {}

    cadastro = Cadastro.objects.get(id_cliente=id_user) 
  
    form = CadastroForm(request.POST or None, instance = cadastro) 
  
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect("/") 
   
    context["form"] = form 
  
    return render(request, "polls/atualizar_perfil.html", context) 

"""def politicas_credito(request, id_ficha):
    context = {}
    ficha = Ficha.objects.get(id=id_ficha)
    cadastro = Cadastro.objects.get(id_cliente=ficha.id_cadastro.id)
    cargo = Cargo.objects.get(id=cadastro.id_cargo.id)
    minimo_cargo = cargo.salario_minimo
    maximo_cargo = cargo.salario_maximo

    form = FichaFormComStatus(request.GET or None, instance = ficha) 

    if form.is_valid():
        if validar_cpf(cadastro.cpf) == 0:
            form.status = 'R'
            #form.motivo = 'O CPF é inválido'
            form.save()
            return HttpResponseRedirect("/") 
        if cadastro.idade < 18:
            form.status = 'R'
            #form.motivo = 'O cliente é menor de idade'
            form.save()
            return HttpResponseRedirect("/")
        if cadastro.renda <= minimo_cargo and cadastro.renda >= maximo_cargo:
            form.status = 'R'
            #form.motivo = 'A renda não é compatível com o cargo - risco de fraude'
            form.save()
            return HttpResponseRedirect("/")
            
            form.status = 'A'
            #form.motivo = 'Aprovado com sucesso'
            form.save()

    return HttpResponseRedirect("/")"""
    
def validar_cpf(cpf):
    i = 10
    soma = 0
    for c in cpf:
        soma += int(c) * i
        i -= 1
        if i < 2:
            break   

    soma *= 10
    soma = soma % 11

    if str(soma) != cpf[9]:
        return 0

    i = 11
    soma = 0
    for c in cpf:
        soma += int(c) * i
        i -= 1
        if i < 2:
            break 
    soma *= 10
    soma = soma % 11

    if str(soma) != cpf[10]:
        return 0

    return 1 

def calcular_risco(cadastro):
    risco = 0

    # Risco conforme a idade
    if cadastro.idade >= 18 and cadastro.idade <= 21:
        risco += 3
    elif cadastro.idade >= 22 and cadastro.idade <= 29:  
        risco += 1
    elif cadastro.idade > 30:
        risco -= 2
    # Somando o risco de acordo com a quantidade de filhos
    if cadastro.qtd_filhos > 0:
        risco += cadastro.qtd_filhos
    else:
        risco -= 1
    # Risco conforme estado civil
    if cadastro.estado_civil != 'Soltero(a)':
        risco += 2
    else:
        risco -= 1
    # Risco conforme tempo de trabalho (em meses)
    if cadastro.tempo_cargo < 36:
        risco += 2
    elif cadastro.tempo_cargo >= 84 and cadastro.tempo_cargo <= 124:
        risco -= 1
    elif cadastro.tempo_cargo > 124:
        risco -= 3
    
    return risco










