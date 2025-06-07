from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tipo(models.Model):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=2, unique=True)
    color = models.CharField(max_length=7, default='#FFFFFF')  # Color en formato hexadecimal

    def __str__(self):
        return self.nombre

class Palabra(models.Model):
    palabra = models.CharField("Vocabulario en chino", max_length=10, db_index=True)
    pinyin = models.CharField(max_length=10)
    traduccion = models.CharField(max_length=200)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT, related_name='palabras', db_index=True)
    nivel_hsk = models.SmallIntegerField(default=1, null=True, blank=True ,db_index=True)
    ejemplo = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vocabulario')

    class Meta:
        unique_together = ('palabra', 'pinyin', 'tipo', 'nivel_hsk', 'usuario')
        ordering = ['nivel_hsk', 'tipo', 'palabra']

    def __str__(self):
        return f"{self.palabra} ({self.usuario.username})"
