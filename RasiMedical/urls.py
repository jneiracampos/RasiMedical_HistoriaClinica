from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('historias/', include('historias_clinicas.urls')),
    path('health/', views.health_check, name='health'),
]
