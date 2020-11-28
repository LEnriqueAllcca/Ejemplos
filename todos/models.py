from django.db import models

# Create your models here.


class Categoria(models.Model):
    categoria = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.categoria
