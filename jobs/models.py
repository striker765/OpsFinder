from django.db import models
from servidores.models import Servidores_CC, Servidores_FastShop
class Job(models.Model):
    job_name = models.CharField(max_length=255, blank=True)
    job_stream = models.CharField(max_length=255, blank=True, null=True)
    workstation = models.CharField(max_length=255, blank=True, null=True)
    aplicacao = models.CharField(max_length=255, blank=True, null=True)
    first_responsible = models.CharField(max_length=255, blank=True, null=True)
    second_responsible = models.CharField(max_length=255, blank=True, null=True)
    third_responsible = models.CharField(max_length=255, blank=True, null=True)
    activation_time = models.CharField(max_length=255, blank=True, null=True)
    criticality = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.job_name or "Nome não definido"


