from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    #path('polls/<int:pk>/', views.FichaDetalhe.as_view(), name='ficha_detalhe'),
    path('polls/cadastro_perfil/', views.CadastroFicha.as_view(), name='cadastro_perfil'),
    path('polls/cadastro_cargo/', views.CadastroCargo.as_view(), name='cadastro_cargo'),
    path('polls/esteira_analise/', views.EsteiraOperador.as_view(), name='esteira_analise'),
    url(r'^atribuir_operador/(?P<id_ficha>\w+)/$', views.atribuirOperador, name='atribuir_operador'),
    url(r'^polls/cadastro_operador/$', views.CadastroOperador, name='cadastro_operador'),
]