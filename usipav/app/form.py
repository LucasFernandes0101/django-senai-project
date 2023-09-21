from django import forms
from django.core import validators
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        
        nome = cleaned_data.get('nome')
        preco = cleaned_data.get('preco')
        quantidade_estoque = cleaned_data.get('quantidade_estoque')
        
        if nome and len(nome) < 2:
            self.add_error('nome', 'O nome do produto deve ter pelo menos 2 caracteres.')
        if nome and len(nome) > 30:
            self.add_error('nome', 'O nome do produto não pode ter mais de 30 caracteres.')
        if preco is not None and preco < 0:
            self.add_error('preco', 'O valor do produto não pode ser negativo.')
        if quantidade_estoque < 0:
            self.add_error('quantidade_estoque', 'A quantidade não pode ser negativa.')        
        return cleaned_data