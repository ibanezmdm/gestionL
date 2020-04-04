from django.shortcuts import render

from django.views import generic

# Create your views here.

class IndexView(generic.TemplateView):
	template_name = "frontend/base.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['site_name'] = 'Gestion Desarrollo'
		return context
