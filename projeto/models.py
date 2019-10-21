from django.db import models

class Autenticacao(models.Model):
    nome = models.CharField(max_length=150)
    email = models.CharField(unique=True, max_length=150)
    password = models.TextField()

    class Meta:
        managed = False
        db_table = 'autenticacao'



class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=15)
    rua = models.TextField()
    cidade = models.CharField(max_length=60)
    estado = models.CharField(max_length=60)
    bairro = models.CharField(max_length=45)
    pais = models.CharField(max_length=45, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    numero = models.CharField(max_length=6, blank=True, null=True)
    latitude = models.TextField(blank=True, null=True)
    longitude = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'
