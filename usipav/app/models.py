from django.db import models

class Topico(models.Model):
    titulo = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo
    
class Pagina(models.Model):
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)
    conteudo = models.TextField()

    def _str__(self):
        return f"Pagina {self.numero_pagina} do topico {self.topico}"

class RegistroAcesso(models.Model):
    pagina = models.ForeignKey(Pagina, on_delete=models.CASCADE)
    data_acesso = models.DateTimeField()

    def __str__(self):
        return f"Acesso a pagina {self.pagina} em {self.data_acesso}"

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    quantidade_estoque = models.IntegerField()

    def __str__(self):
        return self.nome