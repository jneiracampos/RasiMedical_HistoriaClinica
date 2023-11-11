from django.urls import path
from .views import ver_historia_clinica

urlpatterns = [
    path('ver/<int:historia_id>/', ver_historia_clinica, name='ver_historia_clinica'),
]
