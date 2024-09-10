from django.db import models

# Create your models here.
from django.db import models

class Job(models.Model):
    job_name = models.CharField(max_length=255)
    job_stream = models.CharField(max_length=255, blank=True)
    workstation = models.CharField(max_length=255, blank=True)
    first_responsible = models.CharField(max_length=255, blank=True)
    second_responsible = models.CharField(max_length=255, blank=True)
    third_responsible = models.CharField(max_length=255, blank=True)
    activation_time = models.CharField(max_length=255, blank=True)
    criticality = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.job_name



