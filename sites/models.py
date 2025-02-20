from django.db import models
from os import path
from django.core.exceptions import ValidationError
from colorfield.fields import ColorField


def validate_file_extension(value):
    ext = path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.jpeg', '.png', '.svg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


# Create your models here.
class Site(models.Model):
    icone = models.FileField('Image', validators=[validate_file_extension])
    nome = models.CharField(max_length=30)
    descricao = models.TextField()

    cor_de_texto = ColorField(format="hexa")
    cor_de_fundo = ColorField(format="hexa")

    twitter_x = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)


    def __str__(self):
        return self.nome


class Link(models.Model):
    url = models.URLField()
    nome = models.CharField(max_length=100)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome
