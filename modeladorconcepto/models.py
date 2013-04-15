from django.db import models

class radiologico(models.Model):
    QP_ExamGroupCode =  models.CharField(max_length=255)
    QP_ExamGroupDescription = models.CharField(max_length=255)
    QP_ExamCode = models.CharField(max_length=255)
    QP_ExamDescription = models.CharField(max_length=255)
    QP_DateInactive = models.DateTimeField(blank=True, null=True)
    QDoc_ExamCode = models.CharField(max_length=255, primary_key=True)
    QDoc_ExamName = models.CharField(max_length=255)
    QDoc_ExamName2 = models.CharField(max_length=255, blank=True)
    QDoc_GroupedExams = models.CharField(max_length=255)
    QDoc_DateInactive = models.DateTimeField(blank=True, null=True)
    Origin_File = models.CharField(max_length=255)
    revisado = models.BooleanField()
    consultar = models.BooleanField()
    no_pedible = models.BooleanField()
    ambiguo = models.BooleanField()
    observacion = models.CharField(max_length=255, blank=True)
    def __unicode__(self):
        return self.QDoc_ExamName
    class Meta:
        ordering=['QP_ExamGroupCode']