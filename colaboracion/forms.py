from django import forms
from .models import Colaborador, ContactoProveedor

class ContactoProveedorForm(forms.ModelForm):

	class Meta:
		model = ContactoProveedor
		fields = [
			'nombre',
			'apellido',
			'email',
			'en_copia',
		]
		labels = {
			'nombre': 'Nombre',
			'apellido': 'Apellido',
			'email': 'Email',
			'en_copia': 'En copia',
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
			'apellido': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
			'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm'}),
			'en_copia': forms.CheckboxInput(attrs={'class': 'form-control-sm'}),
		}