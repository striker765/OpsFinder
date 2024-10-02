from django.db import models

class Job(models.Model):
    job_name = models.CharField(max_length=255)
    job_stream = models.CharField(max_length=255, blank=True, null=True)
    workstation = models.CharField(max_length=255, blank=True, null=True)
    APLICACAO  = models.CharField(max_length=255, blank=True, null=True)
    first_responsible = models.CharField(max_length=255, blank=True, null=True)
    second_responsible = models.CharField(max_length=255, blank=True, null=True)
    third_responsible = models.CharField(max_length=255, blank=True, null=True)
    activation_time = models.CharField(max_length=255, blank=True, null=True)
    criticality = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.job_name or "Nome não definido"


class Server(models.Model):
    server_name = models.CharField(max_length=255)
    server_cliente = models.CharField(max_length=255)
    datacenter = models.CharField(max_length=255)
    plataforma = models.CharField(max_length=255, default='unknown')
    ip = models.GenericIPAddressField()
    criticidade = models.CharField(max_length=255, default='unknown')
    responsabilidade = models.CharField(max_length=255, default='unknown')
    storage = models.CharField(max_length=255, default='unknown')
    os = models.CharField(max_length=255, default='unknown')
    escalonamento1 = models.CharField(max_length=255, default='unknown')
    escalonamento2 = models.CharField(max_length=255, default='unknown')

    
    def __str__(self):
        return self.server_name or "Nome não definido"