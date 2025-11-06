from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ParticipanteViewSet


urlpatterns = [
    path('', views.index, name='index'),

    # Corridas
    path('corridas/', views.listar_corridas, name='listar_corridas'),
    path('corridas/<int:corrida_id>/inscrever/', views.inscrever_corrida, name='inscrever_corrida'),

    # Participantes
    path('participantes/', views.listar_participantes, name='listar_participantes'),

    path('tabelas/', views.ler_pdf, name='tabelas_corrida'),

]
