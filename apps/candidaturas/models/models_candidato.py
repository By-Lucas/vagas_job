from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from random import choice

from usuarios.models.models_user import ProfileUser
from vagas.models.models_vagas import Vagas

def gerar_codigo():
    tamanho = 14
    valores = '1234567890'
    codigo = ''
    for i in range(tamanho):
        codigo += choice(valores)
    return codigo

class RequisitosCandidatura(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.nome


class EscolaridadeCandidatura(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.nome


class Candidatura(models.Model):
    codigo = models.CharField(max_length=14, default=gerar_codigo, editable=False, unique=True, blank=True, null=True)
    candidato = models.ForeignKey(User, on_delete=models.CASCADE)
    vaga = models.ForeignKey(Vagas, on_delete=models.CASCADE)
    requisitos = models.TextField(max_length=2000, null=True, blank=True)
    requisitos_adicionais = models.ManyToManyField(RequisitosCandidatura, null=True, blank=True)
    escolaridade = models.ForeignKey(EscolaridadeCandidatura, on_delete=models.CASCADE, null=True, blank=True)
    escolhido = models.BooleanField(default=False)
    atualizado_em = models.DateTimeField(default=timezone.now)
    data_cadastro = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return f'{self.candidato} : {self.codigo}'
    
    class Meta():
        db_table = 'candidatura'
        verbose_name = 'candidatura'
        verbose_name_plural = 'candidaturas'