from django.shortcuts import render, get_object_or_404, redirect
from .models import Corrida, Participante
from .forms import ParticipanteForm


def index(request):
    """Página principal do Site"""
    return render(request, 'api_s/index.html')

# CORRIDAS
def listar_corridas(request):
    # Lista todas as corridas cadastradas
    corridas = Corrida.objects.all()
    context = {'corridas': corridas}
    return render(request, 'api_s/listar_corridas.html', context) #Transforma numa pag HTML


# PARTICIPANTES
def listar_participantes(request):
    # Lista todos os participantes cadastrados
    participantes = Participante.objects.select_related('corrida').all()
    context = {'participantes': participantes}
    return render(request, 'api_s/listar_participantes.html', context)


def inscrever_corrida(request, corrida_id):
    # Permite que o usuário se inscreva em uma corrida específica
    corrida = get_object_or_404(Corrida, id=corrida_id)
    
    if request.method == 'POST':
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            participante = form.save(commit=False)
            participante.corrida = corrida  # vincula o participante à corrida
            participante.save()
            return redirect('listar_corridas')  # volta para a lista de corridas
    else:
        form = ParticipanteForm()
    
    context = {'form': form, 'corrida': corrida}
    return render(request, 'api_s/inscrever_corrida.html', context)

from rest_framework import viewsets
from .models import Participante
from .serializers import ParticipanteSerializer

class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer

