from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Publicacao(models.Model):
    titulo = models.CharField(max_length=100)
    descricao_curta = models.TextField(max_length=200, blank=True)
    autor = models.CharField(max_length=100)
    conteudo = models.TextField(max_length=500)
    # imagem = models.ImageField()
    data_cadastro = models.DateTimeField(default=timezone.now)
    categorias = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.titulo


