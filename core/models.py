from django.db import models

class Product(models.Model):
    nome = models.CharField(max_length=255)
    estoque = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
