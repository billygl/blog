# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    usuario = models.CharField(max_length=200)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    TECNOLOGIA  = 'TE'
    ACTUALIDAD = 'AC'
    POLITICA = 'PO'
    ENTRETENIMIENTO = 'EN'
    CATEGORIAS_CHOICES = (
        (TECNOLOGIA, 'Tecnología'),
        (ACTUALIDAD, 'Actualidad'),
        (POLITICA, 'Política'),
        (ENTRETENIMIENTO, 'Entretenimiento')
    )

    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=1000)
    fecha_pub = models.DateTimeField('Fecha publicación', auto_now_add=True)
    fecha_mod = models.DateTimeField(auto_now=True)
    usuario_pub = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=2,
                    choices=CATEGORIAS_CHOICES,
                    default=ACTUALIDAD)

    def __str__(self):
        return self.titulo
