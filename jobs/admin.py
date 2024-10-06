from django.contrib import admin

from django.contrib import admin
from .models import Job 

class JobAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'job_name', 'job_stream', 'workstation', 
        'activation_time', 'criticality', 'descricao'
    )
    search_fields = (
        'id', 'job_name', 'job_stream', 
        'first_responsible', 'descricao'
    )
    list_filter = ('criticality', 'job_stream', 'descricao')
    list_display_links = ('id', 'job_name')

admin.site.register(Job, JobAdmin)

