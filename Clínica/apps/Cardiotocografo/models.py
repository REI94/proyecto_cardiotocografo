from django.db import models
from django.urls import reverse

# Create your models here.
class Historia(models.Model):

    #-----Campos-----
    codigo = models.AutoField('Código', primary_key = True)
    #paciente   Ignorado, falta el modelo Paciente
    #familiar_emr    Ignorado, falta el modelo Persona
    #alergia    Ignorado, falta el modelo Alergia
    enfermedad_padecida = models.CharField('Enfermedad padecida', max_length = 200, blank = False, null = False)
    enfermedad_hereditarias = models.TextField('Enfermedades hereditarias', blank = True)

    #-----Metadata-----
    class Meta:
        ordering = ["codigo", "enfermedad_padecida", "enfermedad_hereditarias"]

    #-----Métodos-----
    def get_absolute_url(self):
        return reverse('detalles-de-historia', args=[str(self.codigo)])

    def __str__(self):
        cadena = "Historia Nro.: "+str(self.codigo)+" - "+self.enfermedad_padecida
        return cadena