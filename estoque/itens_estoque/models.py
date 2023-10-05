from django.db import models

class ItemEstoque(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return self.nome


# Create your models here.
