from django.db import models

class HistoriaClinica(models.Model):
    paciente = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.paciente
