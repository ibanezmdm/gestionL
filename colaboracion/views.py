from django.http import Http404
from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy

from .models import Colaborador, ContactoProveedor
from .forms import ContactoProveedorForm


# Create your views here.

class IndexColaboracionView(generic.ListView):
	template_name = "colaboracion/index.html"
	model = Colaborador
	
	# TODO: Generera variables de contexto de forma automatica
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['site_name'] = 'Gestion | Colaboracion'
		return context


class DetalleProveedorView(generic.DeleteView):
	template_name = "colaboracion/detalleProveedor.html"
	model = Colaborador

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['site_name'] = 'Gestion | Colaboracion'
		return context


class ContactoProveedorUpdateView(generic.UpdateView):
	model = ContactoProveedor
	form_class = ContactoProveedorForm

	def get_success_url(self):
		if 'rut' in self.kwargs.keys():
			return reverse_lazy('colaboracion:proveedor', args=[self.kwargs['rut']])
		else:
			return reverse_lazy('colaboracion:index')


def borraContactoDeProveedor(request, rut, email):
	try:
		prov = Colaborador.objects.get(proveedor = rut)
		contacto = prov.contactoproveedor_set.get(email = email)
		prov.contactoproveedor_set.remove(contacto)
	except:
		raise Http404("Registro no Existe")
	
	return redirect(reverse_lazy('colaboracion:proveedor', args=[rut]))


def agregaContactoDeProveedor(request, rut, email):

	prov = Colaborador.objects.get(proveedor = rut)
	try:
		contacto = ContactoProveedor.objects.get(email = email)
	except ContactoProveedor.DoesNotExist:
		contacto = ContactoProveedor(email=email)
		contacto.save()
		
	prov.contactoproveedor_set.add(contacto)
	
	return redirect(reverse_lazy('colaboracion:proveedor', args=[rut]))