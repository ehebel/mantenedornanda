from django.db import models
from django.forms import ModelForm

# Create your models here.
class ciediez(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    descriptor = models.CharField(max_length=255)
    capitulo_num = models.CharField(max_length=10, null=True, blank=True)
    capitulo_titulo = models.CharField(max_length=255, null=True, blank=True)
    grupo = models.CharField(max_length=255, null=True, blank=True)
    categoria = models.CharField(max_length=255, null=True, blank=True)
    version = models.CharField(max_length=255, null=True, blank=True)
    def __unicode__(self):
        return self.descriptor
    class Meta:
        ordering=['codigo']

class casprocedimiento(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    estado = models.CharField(max_length=20)
    fecha = models.DateField()
    usuario_crea = models.CharField(max_length=40)
    usuario_modif = models.CharField(max_length=40)

class casdiagnostico(models.Model):
    codigo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=255)
    estado = models.CharField(max_length=20)
    fecha = models.DateField()
    usuario_crea = models.CharField(max_length=40)
    usuario_modif = models.CharField(max_length=40, null=True, blank=True)
    def __unicode__(self):
        return self.descripcion
    class Meta:
        ordering = ['codigo']

class ges_patologia(models.Model):
    id = models.IntegerField(primary_key=True)
    glosa = models.CharField(max_length=255)
    ciediez = models.ManyToManyField(ciediez)
    casproc = models.ManyToManyField(casprocedimiento)
    casdiag = models.ManyToManyField(casdiagnostico)
    def __unicode__(self):
        return self.glosa
    class Meta:
        ordering = ['id']


class GESform(ModelForm):
    class Meta:
        model = ges_patologia