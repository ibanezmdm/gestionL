from django.db import models
from proveedores.models import Proveedor, TimestampModel


# Create your models here.

class Colaborador(TimestampModel):
	proveedor = models.OneToOneField(Proveedor, on_delete = models.PROTECT, primary_key = True)
	estado = models.BooleanField(default = True)

	class Meta:
		verbose_name_plural = 'Proveedores Colaboración'
		ordering = ['proveedor']

	def __str__(self):
		return '%s'% (self.proveedor)



class ContactoProveedor(TimestampModel):
	proveedor = models.ManyToManyField(Colaborador)
	nombre = models.CharField(max_length = 50, null = True, blank = True)
	apellido = models.CharField(max_length = 50, null = True, blank = True)
	email = models.EmailField(primary_key = True)
	en_copia = models.BooleanField(default = False)

	class Meta:
		verbose_name_plural = 'Contactos Proveedores'
		ordering = ['email']
	
	def __str__(self):
		return '%s'% (self.email)