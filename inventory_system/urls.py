from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="Pagina 01"),
    path('paginaTeste/', views.paginaTeste, name="Pagina Teste"),
]
