from django.db import models


# Create your models here.

class Restaurante(models.Model):
    nome = models.CharField(max_length=100)
    local = models.CharField(max_length=200)
    cardapio = models.CharField(max_length=100)
    horario = models.DateTimeField()
    thumb = models.ImageField(upload_to='imagens')
    descricao = models.TextField(max_length=1000)

    def __str__(self):
        return self.nome
