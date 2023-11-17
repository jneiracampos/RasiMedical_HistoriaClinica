from django.urls import path
from .views import obtener_historia_clinica

urlpatterns = [
    path('obtener_historia_clinica/<int:historia_id>/<int:doctor_id>/', obtener_historia_clinica, name='obtener_historia_clinica'),
    # Otras rutas URL
]
