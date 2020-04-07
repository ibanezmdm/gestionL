from django.db import models
from proveedores.models import Proveedor, TimestampModel


# Create your models here.

class ContactoProveedorManager(models.Manager):

	def destinatario(self):
		return self.filter(en_copia=False)

	def destinatarios_list(self):
		qs = self.destinatario()
		if len(qs) > 0:
			correos = set(c.email for c in qs) # genera una lista a partir del queryset
			return '; '.join('<{}>'.format(c) for c in correos) # Combierte la lista en un array separado por ' ;'
		return None

	def en_copia(self):
		return self.filter(en_copia=True)

	def en_copia_list(self):
		qs = self.en_copia()
		if len(qs) > 0:
			correos = set(c.email for c in qs) # genera una lista a partir del queryset
			return '; '.join('<{}>'.format(c) for c in correos) # Combierte la lista en un array separado por ' ;'
		return None


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
	nombre = models.CharField(max_length = 50, blank = True, default = '')
	apellido = models.CharField(max_length = 50, blank = True, default = '')
	email = models.EmailField(primary_key = True)
	en_copia = models.BooleanField(default = False)

	objects = ContactoProveedorManager()
	
	class Meta:
		verbose_name_plural = 'Contactos Proveedores'
		ordering = ['en_copia', 'email']
	
	def __str__(self):
		return '%s'% (self.email)