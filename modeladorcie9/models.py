from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class cas_concepto(models.Model):
    idconcepto = models.BigIntegerField()
    estado = models.BooleanField(default=0)
    descripcioncompleta = models.CharField(max_length=255)
    usuario_ultima_modificacion = models.ForeignKey(User, related_name='relacion_usuario_modificacion')
    fecha_ultima_modificacion = models.DateTimeField(auto_now=True, blank=True)
    usuario_creacion = models.ForeignKey(User, related_name='relacion_usuario_creacion')
    fecha_creacion = models.DateTimeField()
    usuario_baja = models.ForeignKey(User, null=True, related_name='relacion_usuario_baja')
    fecha_baja = models.DateTimeField(null = True)
    def __unicode__(self):
        return self.descripcioncompleta
    class Meta:
        ordering=['descripcioncompleta']

class cas_descripcion(models.Model):
    OPCIONES_TIPO = (
        (1,'Preferido'),
        (2,'Sinonimo Visible'),
        (3,'Descripcion Completa'),
        (4,'Error tipografico'),
        )
    iddescripcion = models.BigIntegerField()
    estado = models.BooleanField(default=0)
    idconcepto = models.ForeignKey(cas_concepto)
    termino = models.CharField(max_length=255)
    tipodescripcion = models.IntegerField(choices=OPCIONES_TIPO)
    def __unicode__(self):
        return self.iddescripcion
    class Meta:
        ordering=['iddescripcion']

class cas_conj_mapeo(models.Model):
    idmapset = models.BigIntegerField() #autoincremetar
    nombremapset = models.CharField(max_length=255)
    tipomapset = models.IntegerField()
    nombrecompleto = models.CharField(max_length=255)
    separadormapset = models.CharField(max_length=255)
    reglamapset = models.CharField(max_length=255)


class cas_mapsalida(models.Model):
    codigo = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=255)
    idmapset = models.ForeignKey(cas_conj_mapeo)

class cas_mapdestino(models.Model):
    idmapdestino=models.BigIntegerField(primary_key=True)
    mapcodigo = models.ManyToManyField(cas_mapsalida)

class cas_mapeo(models.Model):
    idmapset = models.ForeignKey(cas_conj_mapeo)
    mapidconcepto = models.ForeignKey(cas_concepto)
    mapopcion = models.IntegerField()
    mapprioridad = models.IntegerField()
    mapdestino = models.ForeignKey(cas_mapdestino)
    mapregla = models.CharField(max_length=255)
    mapadvertencia = models.IntegerField()
    def __unicode__(self):
        return self.idmapset
    class Meta:
        ordering=['idmapset']

class cienueve(models.Model):
    codigo = models.CharField(max_length=10)
    descriptor = models.CharField(max_length=255)
    area = models.CharField(max_length=5)
    clasificacion = models.CharField(max_length=5)
    def __unicode__(self):
        return self.descriptor
    class Meta:
        ordering=['codigo']


class cas_procedimiento(models.Model):
    idintervencionclinica = models.CharField(max_length=20)
    integlosa = models.CharField(max_length=255)
    codgrupo = models.CharField(max_length=10)
    grpdescripcion = models.CharField(max_length=255)
    codsubgrupo = models.CharField(max_length=10)
    sgrdescripcion = models.CharField(max_length=255)
    inte_codigo_fonasa =  models.CharField(max_length=10)
    cienueve = models.ManyToManyField(cienueve)
    revisado = models.BooleanField()
    def __unicode__(self):
        return self.integlosa
    class Meta:
        ordering=['id']

#tabla transitoria de descripciones de CAS procedimiento para tener sinonimo
class cas_procedimiento_desc(models.Model):
    OPCIONES_TIPO = (
        (1,'Preferido'),
        (2,'Sinonimo Visible'),
        (3,'Descripcion Completa'),
        (4,'Error tipografico'),
        )
    estado = models.BooleanField(default=0)
    idconcepto = models.ForeignKey(cas_procedimiento)
    termino = models.CharField(max_length=255)
    tipodescripcion = models.IntegerField(choices=OPCIONES_TIPO)
    def __unicode__(self):
        return self.termino
    class Meta:
        ordering=['id']

class cas_procedimiento_cienueve(models.Model):
    cas_procedimiento_id = models.ForeignKey(cas_procedimiento)
    cienueve_id = models.ForeignKey(cienueve)
