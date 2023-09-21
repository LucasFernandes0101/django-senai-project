from django.shortcuts import render
from django.http import HttpResponse
from .models import RegistroAcesso,Produto
from . import form
from django import forms
from .form import ProdutoForm

def registro_acesso(request):
    context = {
        'acessos': RegistroAcesso.objects.all()
    }
    return render(request, 'registroacesso.html', context)

def index(request):
    return render(request, 'home.html')

def calculadora(request):
    return render(request, 'calculadora.html') 

def linguagens(request):
    return render(request, 'linguagens.html') 

def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        print("Erro. Campos Invalidos")
        form = ProdutoForm()
    
    return render(request, 'criar_produto.html', {'form': form})


def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'produtos': produtos})