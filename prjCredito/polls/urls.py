from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    #path('polls/<int:pk>/', views.FichaDetalhe.as_view(), name='ficha_detalhe'),
    path('polls/ficha/', views.CadastroFicha.as_view(), name='ficha'),
]