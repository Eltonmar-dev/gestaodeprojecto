from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('projetos/', views.lista_projetos, name='lista_projetos'),
    path('biblioteca/', views.lista_biblioteca, name='lista_biblioteca'),
    
    # Rotas de Ação
    path('projeto/ocultar/<int:pk>/', views.ocultar_projeto, name='ocultar_projeto'),
    path('projeto/eliminar/<int:pk>/', views.eliminar_projeto, name='eliminar_projeto'),
    path('biblioteca/ocultar/<int:pk>/', views.ocultar_material, name='ocultar_material'),
]