# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('seleccionar_historia/', views.seleccionar_historia, name='seleccionar_historia'),
    path('obtener_historia_clinica/<int:historia_id>/', views.obtener_historia_clinica, name='obtener_historia_clinica'),
]
