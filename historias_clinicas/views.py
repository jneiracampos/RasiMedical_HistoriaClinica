from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import HistoriaClinica, Doctor
from django.shortcuts import render

def obtener_historia_clinica(request, historia_id, doctor_id):
    historia_clinica = get_object_or_404(HistoriaClinica, pk=historia_id)
    doctor = get_object_or_404(Doctor, pk=doctor_id)

    if historia_clinica.doctor == doctor:
        data = {
            'paciente': historia_clinica.paciente.nombre,
            'descripcion': historia_clinica.descripcion,
            'fecha_creacion': historia_clinica.fecha_creacion,
            'doctor': historia_clinica.doctor.nombre
        }
        return render(request, 'historia_clinica.html', {'data': data})
    else:
        return JsonResponse({'error': 'El doctor no tiene acceso a esta historia clínica.'}, status=403)
