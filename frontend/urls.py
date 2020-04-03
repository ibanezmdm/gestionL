from django.urls import path
from . import views


# app_name = 'gestiondesarrollo'
urlpatterns = [
	# ** Ej: /gestiondesarrollo/
	path('gestiondesarrollo/', views.IndexView.as_view(), name="index")
]
