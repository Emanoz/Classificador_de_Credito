from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from . models import Ficha, Cadastro
from django.contrib import messages
from .forms import CadastroForm, FichaForm
from django import forms
from django.contrib.auth.decorators import login_required
# Create your views here.

class Dashboard(ListView):
    model = Ficha
    template_name = 'polls/dashboard.html'

class CadastroFicha(CreateView):
    model = Cadastro
    template_name = 'polls/ficha.html'
    fields = "__all__"
    success_url = "/"