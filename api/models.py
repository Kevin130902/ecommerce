from django.db import models

class Produto(models.Model):
    tituloProduto = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(max_length=500)
    imagemProduto = models.CharField(max_length=255)
    categoriaProduto = models.CharField(max_length=255)
    classProduto = models.CharField(max_length=255)
    exibirNome = models.BooleanField(default=True)
