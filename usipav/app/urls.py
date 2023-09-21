from django.urls import path

from . import views

app_name = "app"
urlpatterns = [
    path("", views.index, name="index"),
    path("calculadora/", views.calculadora, name="calculadora"),
    path("linguagens/", views.linguagens, name="linguagens"), 
    path('registro-acessos/', views.registro_acesso, name='registro-acesso'),
    path('produto/', views.criar_produto, name='criar-produto'),
    path('produto/listar/', views.lista_produtos, name='lista-produtos')
]
