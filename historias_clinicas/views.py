# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from .models import HistoriaClinica, Doctor

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('seleccionar_historia')
        else:
            return render(request, 'login.html', {'error': 'Credenciales incorrectas.'})
    return render(request, 'login.html')

@login_required
def seleccionar_historia(request):
    historias_clinicas = HistoriaClinica.objects.filter(doctor=request.user.doctor)
    return render(request, 'seleccionar_historia.html', {'historias_clinicas': historias_clinicas})

@login_required
def obtener_historia_clinica(request, historia_id):
    historia_clinica = get_object_or_404(HistoriaClinica, pk=historia_id, doctor=request.user.doctor)
    data = {
        'paciente': historia_clinica.paciente.nombre,
        'descripcion': historia_clinica.descripcion,
        'fecha_creacion': historia_clinica.fecha_creacion,
        'doctor': historia_clinica.doctor.nombre
    }
    return render(request, 'historia_clinica.html', {'data': data})
