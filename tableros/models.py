from django.db import models
from proveedores.models import TimestampModel

# Create your models here.

class Categoria(TimestampModel):
	nombre = models.CharField(max_length = 50)
	
	class Meta:
		verbose_name_plural = 'Categorias'
		ordering = ['nombre']

	def __str__(self):
		return '%s'% (self.nombre)


class Tablero(TimestampModel):
	nombre = models.CharField(max_length = 50)
	script = models.CharField(max_length = 1000)
	categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

	class Meta:
		verbose_name_plural = 'Tableros'
		ordering = ['categoria', 'nombre']

	def __str__(self):
		return '%s'% (self.nombre)