from django.urls import path, reverse_lazy
from django.contrib.auth import views

app_name='accounts'
urlpatterns = [
	path('login/', views.LoginView.as_view(), name='login'),
	path('logout/', views.LogoutView.as_view(), name='logout'),
	path('password_change/', views.PasswordChangeView.as_view(success_url=reverse_lazy('gestiondesarrollo:index')), name='password_change'),
]

