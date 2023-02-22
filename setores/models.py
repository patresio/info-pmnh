from django.db import models

# Create your models here.


class Diretoria(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome


class Setor(models.Model):
    diretoria = models.ForeignKey(
        Diretoria, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=200, null=True, blank=True)
    responsavel = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nome
