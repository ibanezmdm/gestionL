from django.urls import path
from . import views

app_name = 'colaboracion'
urlpatterns = [
		path('', views.IndexColaboracionView.as_view(), name='index'),
		path('<int:pk>/', views.DetalleProveedorView.as_view(), name="proveedor"),
		path('<pk>/edit', views.ContactoProveedorUpdateView.as_view(), name="contact_edit"),
		path('<int:rut>/<pk>/edit', views.ContactoProveedorUpdateView.as_view(), name="prov_contact_edit"),
		path('<int:rut>/<email>/delete', views.borraContactoDeProveedor, name="prov_contact_delete"),
		path('<int:rut>/<email>/add', views.agregaContactoDeProveedor, name="prov_contact_add"),
]
