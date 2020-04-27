from django.shortcuts import render
from django.views import generic

from .models import Categoria, Tablero

# Create your views here.
class IndexTablerosListView(generic.ListView):
	model = Categoria
	template_name = 'tableros/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['site_name'] = 'Gestion | Tableros'
		return context


class TablerosDeatalView(generic.DetailView):
	model = Tablero

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['site_name'] = 'Gestion | Tableros'
		return context