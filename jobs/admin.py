from django.contrib import admin

from django.contrib import admin
from .models import Job , Server

class JobAdmin(admin.ModelAdmin):
    list_display = ('id','job_name', 'job_stream', 'workstation', 'activation_time', 'criticality')
    search_fields = ('id','job_name', 'job_stream','first_responsible')
    list_filter = ('criticality', 'job_stream',)
    list_display_links = ('job_name',)

admin.site.register(Job, JobAdmin)


class ServerAdmin(admin.ModelAdmin):
    list_display = ('id', 'server_name', 'server_cliente', 'datacenter', 'plataforma', 'ip', 'criticidade', 'responsabilidade', 'escalonamento1', 'escalonamento2')
    list_display_links = ('id', 'server_name', )

admin.site.register(Server, ServerAdmin) 