from django.urls import path
from . import views


app_name = 'tableros'
urlpatterns = [
		path('', views.IndexTablerosListView.as_view(), name='index'),
		path('<int:pk>/detail', views.TablerosDeatalView.as_view(), name='tablero')
]