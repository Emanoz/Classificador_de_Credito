from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
]


# path('signup/', views.SignUpView.as_view(), name='signup'),
