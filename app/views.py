from django.shortcuts import render
from django.views import View
from .models import *

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html',)
    
    def post(self, request):
        pass

class LivrosView(View):
    def get(self, request):
        livros = Livro.objects.all()
        return render(request, 'livros.html', {'livros': livros})

    def post(self, request):
        pass


class GenerosView(View):
    def get(self, request):
        generos = Genero.objects.all()
        return render(request, 'generos.html', {'generos': generos})

    def post(self, request):
        pass

class AutoresView(View):
    def get(self, request):
        autores = Autor.objects.all()
        return render(request, 'autores.html', {'autores': autores})

    def post(self, request):
        pass

class EditorasView(View):
    def get(self, request):
        editoras = Editora.objects.all()
        return render(request, 'editoras.html', {'editoras': editoras})

    def post(self, request):
        pass

class UsuariosView(View):
    def get(self, request,):
        usuarios = Usuario.objects.all()
        return render(request, 'usuarios.html',{'usuarios': usuarios})
    
    def post(self, request):
        pass

class CidadesView(View):
    def get(self, request):
        cidades = Cidade.objects.all()
        return render(request, 'cidades.html', {'cidades': cidades})

    def post(self, request):
        pass

class EmprestimoView(View):
    def get(self, request):
        reservas = Emprestimo.objects.all()
        return render(request, 'reserva.html',{'reservas': reservas})

    def post(self, request):
        pass

