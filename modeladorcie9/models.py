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

class ciediez(models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    descriptor = models.CharField(max_length=255)
    capitulo_num = models.CharField(max_length=10)
    capitulo_titulo = models.CharField(max_length=255)
    grupo = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    def __unicode__(self):
        return self.descriptor
    class Meta:
        ordering=['codigo']


class cas_procedimiento(models.Model):
    idintervencionclinica = models.CharField('ID CAS',max_length=20, primary_key= True)
    integlosa = models.CharField(max_length=255)
    codgrupo = models.CharField(max_length=10)
    grpdescripcion = models.CharField(max_length=255)
    codsubgrupo = models.CharField(max_length=10)
    sgrdescripcion = models.CharField(max_length=255)
    inte_codigo_fonasa =  models.CharField(max_length=10)
    cienueve = models.ManyToManyField(cienueve, blank=True)
    revisado = models.BooleanField()
    observaciones = models.CharField(max_length=255, blank=True)
    incodificable = models.BooleanField()
    consultar = models.BooleanField(default=False)
    def __unicode__(self):
        return self.integlosa
    class Meta:
        ordering=['idintervencionclinica']

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


class cas_dbnet_ppio_activo(models.Model):
    cod_principio_activo    = models.IntegerField(primary_key=True)
    principio_activo        = models.CharField(max_length=255)
    def __unicode__(self):
        return self.principio_activo

class cas_dbnet_ax_farmacol(models.Model):
    cod_acc_farmacologica	= models.IntegerField(primary_key=True)
    accion_farmacologica    = models.CharField(max_length=255)
    def __unicode__(self):
        return self.accion_farmacologica

class cas_dbnet_producto(models.Model):
    cod_clasificacion = models.IntegerField()
    clasificacion = models.CharField(max_length=255)
    codigo = models.CharField(max_length=10, primary_key=True)
    producto = models.CharField(max_length=255)
    receta_retenida = models.BooleanField(default=False, blank=True)
    cod_principio_activo = models.ForeignKey(cas_dbnet_ppio_activo) #foreign key
    principio_activo = models.CharField(max_length=255)
    cod_concentracion = models.CharField(max_length=10)
    concentracion = models.CharField(max_length=255)
    cod_acc_farmacologica = models.ForeignKey(cas_dbnet_ax_farmacol)
    accion_farmacologica = models.CharField(max_length=255)
    cod_unidad = models.CharField(max_length=10)
    unidad_medida = models.CharField(max_length=255)
    def __unicode__(self):
        return self.producto

class cas_kairos_ax_terapeut(models.Model):
    accionesterapeuticas_clave	= models.IntegerField(primary_key=True)
    accionesterapeuticas_descripcion = models.CharField(max_length=255)
    def __unicode__(self):
        return self.accionesterapeuticas_descripcion

class cas_kairos_sustancia(models.Model):
    sustancia_clave = models.IntegerField(primary_key=True)
    sustancia_descripcion = models.CharField(max_length=255)
    def __unicode__(self):
        return self.sustancia_descripcion

class cas_kairos_producto(models.Model):
    productos_clave	= models.IntegerField(primary_key=True)
    productos_descripcion = models.CharField(max_length=255)
    presentaciones_descripcion	= models.CharField(max_length=255)
    clavepresentacion	= models.IntegerField()
    concentracion	= models.CharField(max_length=40)
    unidadconcentracion	= models.CharField(max_length=40)
    especificacion	= models.CharField(max_length=255)
    viaadministracion	= models.CharField(max_length=40)
    medio = models.CharField(max_length=40)
    cantidadenvase = models.IntegerField()
    dosis = models.IntegerField()
    cantidadunidad = models.IntegerField()
    laboratorios_clave = models.IntegerField()
    abreviatura = models.CharField(max_length=255)
    laboratorios_descripcion = models.CharField(max_length=255)
    ax_terapeut = models.ManyToManyField(cas_kairos_ax_terapeut, through='cas_kairos_relacion_producto_ax')
    sustancia =  models.ManyToManyField(cas_kairos_sustancia, through='cas_kairos_relacion_producto_sustancia')
    def __unicode__(self):
        return self.productos_descripcion

class cas_term_vtm_vmp(models.Model):
    descriptionid_vtm = models.CharField(max_length=20)
    vtm = models.CharField(max_length=255)
    descriptionid_vmp = models.CharField(max_length=20,primary_key=True)
    vmp = models.CharField(max_length=255)
    desconocido = models.BooleanField(default=False, blank=True)
    revisado = models.BooleanField(default=False, blank=True)
    arsenal = models.BooleanField(default=False, blank=True)
    consultar = models.BooleanField(default=False, blank=True)
    cambio_nombre = models.BooleanField(default=False, blank=True)
    observacion = models.CharField(max_length=255, blank=True)
    dbnet = models.ManyToManyField(cas_dbnet_producto, blank=True)
    kairos = models.ManyToManyField(cas_kairos_producto, blank=True)
    def __unicode__(self):
        return self.vtm

class cas_kairos_relacion_producto_ax(models.Model):
    producto_clave = models.ForeignKey(cas_kairos_producto)
    accionesterapeuticas_clave = models.ForeignKey(cas_kairos_ax_terapeut, unique=True)
    importancia = models.IntegerField()

class cas_kairos_relacion_producto_sustancia(models.Model):
    producto_clave = models.ForeignKey(cas_kairos_producto)
    sustancia_clave = models.ForeignKey(cas_kairos_sustancia)
    importancia = models.IntegerField()




