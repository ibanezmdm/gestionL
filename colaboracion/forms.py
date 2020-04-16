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
			'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm', 'readonly':'readonly'}),
			'en_copia': forms.CheckboxInput(attrs={'class': 'form-control-sm'}),
		}


class ColaboradorForm(forms.ModelForm):

	class Meta:
		model = Colaborador
		fields = ['proveedor']
		labels = {
			'proveedor': 'Proveedor',
		}
		widgets = {
			'proveedor': forms.Select(attrs={'class': 'select2AddColaborador form-control', 'style':'width: 100%;'}),
		}