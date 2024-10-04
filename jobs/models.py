from django.db import models


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


class Cc_server(models.Model):
    server_name = models.CharField(max_length=255, blank=True)
    server_cliente = models.CharField(max_length=255, blank=True)
    datacenter = models.CharField(max_length=255, blank=True)
    plataforma = models.CharField(max_length=255, default='unknown', blank=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    criticidade = models.CharField(max_length=255, default='unknown', blank=True)
    responsabilidade = models.CharField(max_length=255, default='unknown', blank=True)
    storage = models.CharField(max_length=255, default='unknown', blank=True)
    os = models.CharField(max_length=255, default='unknown', blank=True)
    escalonamento1 = models.CharField(max_length=255, default='unknown', blank=True)
    escalonamento2 = models.CharField(max_length=255, default='unknown', blank=True)

    def __str__(self):
        return self.server_name or "Nome não definido"


class Cc_fast(models.Model):
    server_name = models.CharField(max_length=255, blank=True)
    server_cliente = models.CharField(max_length=255, blank=True)
    datacenter = models.CharField(max_length=255, blank=True)
    plataforma = models.CharField(max_length=255, default='unknown', blank=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    criticidade = models.CharField(max_length=255, default='unknown', blank=True)
    responsabilidade = models.CharField(max_length=255, default='unknown', blank=True)
    storage = models.CharField(max_length=255, default='unknown', blank=True)
    os = models.CharField(max_length=255, default='unknown', blank=True)
    escalonamento1 = models.CharField(max_length=255, default='unknown', blank=True)
    escalonamento2 = models.CharField(max_length=255, default='unknown', blank=True)

    def __str__(self):
        return self.server_name or "Nome não definido"

