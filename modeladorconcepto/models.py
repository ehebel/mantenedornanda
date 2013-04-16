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



class loinc(models.Model):
    loinc_num = models.CharField(max_length=10 , primary_key=True, null=True)
    component = models.CharField(max_length=255 , null=True)
    property = models.CharField(max_length=30 , null=True)
    time_aspct = models.CharField(max_length=15 , null=True)
    system = models.CharField(max_length=100 , null=True)
    scale_typ = models.CharField(max_length=30 , null=True)
    method_typ = models.CharField(max_length=50 , null=True)
    _class = models.CharField(max_length=20 , null=True)
    source = models.CharField(max_length=8 , null=True)
    chng_type = models.CharField(max_length=3 , null=True)
    comments = models.TextField()
    status = models.CharField(max_length=11 , null=True)
    consumer_name = models.CharField(max_length=255 , null=True)
    molar_mass = models.CharField(max_length=13 , null=True)
    classtype = models.CharField(max_length=11 , null=True)
    formula = models.CharField(max_length=255 , null=True)
    species = models.CharField(max_length=20 , null=True)
    exmpl_answers =models.TextField()
    acssym = models.TextField()
    base_name = models.CharField(max_length=50 , null=True)
    naaccr_id = models.CharField(max_length=20 , null=True)
    code_table = models.CharField(max_length=10 , null=True)
    survey_quest_text = models.TextField()
    survey_quest_src = models.CharField(max_length=50 , null=True)
    unitsrequired = models.CharField(max_length=1 , null=True)
    submitted_units = models.CharField(max_length=30 , null=True)
    relatednames2 = models.TextField()
    shortname = models.CharField(max_length=40 , null=True)
    order_obs = models.CharField(max_length=15 , null=True)
    cdisc_common_tests = models.CharField(max_length=1 , null=True)
    hl7_field_subfield_id = models.CharField(max_length=50 , null=True)
    external_copyright_notice = models.TextField()
    example_units = models.CharField(max_length=255 , null=True)
    long_common_name = models.CharField(max_length=255 , null=True)
    hl7_v2_datatype = models.CharField(max_length=255 , null=True)
    hl7_v3_datatype = models.CharField(max_length=255 , null=True)
    curated_range_and_units = models.TextField()
    document_section = models.CharField(max_length=255 , null=True)
    example_ucum_units = models.CharField(max_length=255 , null=True)
    example_si_ucum_units = models.CharField(max_length=255 , null=True)
    status_reason = models.CharField(max_length=9 , null=True)
    status_text = models.TextField()
    change_reason_public = models.IntegerField(null=True)
    common_test_rank = models.IntegerField(null= True)
    common_order_rank = models.IntegerField(null=True)
    common_si_test_rank = models.IntegerField(null=True)
    hl7_attachment_structure = models.CharField(max_length=15 , null=True)
    def __unicode__(self):
        return self.component


class source_organization(models.Model):
    copyright_id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    copyright = models.TextField()
    terms_of_use = models.TextField()
    url = models.CharField(max_length=255)
    def __unicode__(self):
        return  self.name


class map_to(models.Model):
    loinc  = models.CharField(max_length=10 , null=True)
    map_to  = models.CharField(max_length=10 , null=True)
    comment = models.TextField()
    def __unicode__(self):
        return self.loinc
