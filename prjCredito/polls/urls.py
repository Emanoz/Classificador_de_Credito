from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    #path('polls/<int:pk>/', views.FichaDetalhe.as_view(), name='ficha_detalhe'),
    path('polls/cadastro_perfil/', views.CadastroFicha.as_view(), name='cadastro_perfil'),
    path('polls/cadastro_cargo/', views.CadastroCargo.as_view(), name='cadastro_cargo'),
    url(r'^polls/cadastro_operador/$', views.CadastroOperador, name='cadastro_operador'),
]