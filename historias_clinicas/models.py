from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} - {self.nombre}'

class Doctor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id} - {self.nombre}'

class HistoriaClinica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, default=1)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} - {self.paciente} - {self.doctor}'
