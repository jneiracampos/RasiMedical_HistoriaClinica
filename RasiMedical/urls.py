from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('historias/', include('historias_clinicas.urls')),
]
