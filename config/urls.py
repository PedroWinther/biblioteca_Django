"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="index"),
    path('livros/', LivrosView.as_view(), name="livros"),
    path('generos/', GenerosView.as_view(), name="generos"),
    path('autores/', AutoresView.as_view(), name="autores"),
    path('editoras/', EditorasView.as_view(), name="editoras"),
    path('usuarios/', UsuariosView.as_view(), name="usuarios"),
    path('reserva/', EmprestimoView.as_view(),name='reserva'),
    path('cidade/', CidadesView.as_view(),name='cidade'),

]
