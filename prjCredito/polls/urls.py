from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('polls/<int:pk>/', views.FichaDetalhe.as_view(), name='detalhes_ficha'),
    path('polls/cadastro_perfil/', views.CadastroFicha.as_view(), name='cadastro_perfil'),
    path('polls/cadastro_cargo/', views.CadastroCargo.as_view(), name='cadastro_cargo'),
    path('polls/listar_cargos/', views.ListarCargos.as_view(), name='lista_cargos'),
    path('polls/listar_operadores/', views.ListarOperadores.as_view(), name='listar_operadores'),
    path('polls/esteira_analise/', views.EsteiraOperador.as_view(), name='esteira_analise'),
    path('polls/verificar_cadastro/', views.verificar_cadastro, name='verificar_cadastro'),
    path('polls/solicitar_ficha/', views.solicitar_ficha, name='solicitar_ficha'),
    #url(r'^polls/politicas_credito/(?P<id_ficha>\w+)/$', views.politicas_credito, name='politicas_credito'),
    url(r'^atribuir_operador/(?P<id_ficha>\w+)/$', views.atribuirOperador, name='atribuir_operador'),
    url(r'^atualizar_perfil/(?P<id_user>\w+)/$', views.atualizar_perfil, name='atualizar_perfil'),
    url(r'^excluir_cargo/(?P<id_cargo>\w+)/$', views.excluir_cargo, name='excluir_cargo'),
    url(r'^atualizar_cargo/(?P<id_cargo>\w+)/$', views.atualizar_cargo, name='atualizar_cargo'),
    url(r'^polls/cadastro_operador/$', views.CadastroOperador, name='cadastro_operador'),
    url(r'^excluir_operador/(?P<id_operador>\w+)/$', views.excluir_operador, name='excluir_operador'),
    url(r'^atualizar_operador/(?P<id_operador>\w+)/$', views.atualizar_operador, name='atualizar_operador'),
] 