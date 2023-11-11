# historias_clinicas/views.py
from django.shortcuts import render
from .models import HistoriaClinica

def ver_historia_clinica(request, historia_id):
    historia = HistoriaClinica.objects.get(pk=historia_id)
    return render(request, 'ver_historia.html', {'historia': historia})
