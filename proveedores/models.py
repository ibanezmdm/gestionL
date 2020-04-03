from django.db import models

# Create your models here.

class TimestampModel(models.Model):
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	class Meta:
		abstract = True	


class Proveedor(TimestampModel):
	id = models.IntegerField(primary_key = True)
	codigo = models.IntegerField(unique = True)
	rut = models.IntegerField(unique = True)
	razon_social = models.CharField(max_length = 50)

	class Meta:
		verbose_name_plural = 'Proveedores'
		ordering = ['razon_social']
	
	def __str__(self):
		return '%s'% (self.razon_social)