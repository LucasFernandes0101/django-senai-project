import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first.settings')
django.setup()

from app.models import Topico, Pagina, RegistroAcesso
from faker import Faker
from datetime import datetime
import random

fake = Faker()

# Criar tópicos
topicos = []
for _ in range(10):
    titulo = fake.company()
    topico = Topico.objects.create(titulo=titulo)
    topicos.append(topico)

# Criar páginas e registros de acesso
for topico in topicos:
    num_paginas = random.randint(5, 15)  # Número aleatório de páginas por tópico

    for numero_pagina in range(1, num_paginas + 1):
        conteudo = fake.paragraphs(nb=3, ext_word_list=None)
        pagina = Pagina.objects.create(topico=topico, conteudo='\n'.join(conteudo))

        num_acessos = random.randint(1, 20)  # Número aleatório de acessos por página

        for _ in range(num_acessos):
            RegistroAcesso.objects.create(pagina=pagina, data_acesso=datetime.now())

print("Dados falsos criados com sucesso!")