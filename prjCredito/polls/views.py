from django.shortcuts import render
from django.views.generic import ListView
from . models import Cadastro
# Create your views here.

class Home(ListView):
    model = Cadastro
    template_name = 'polls/home.html'
