from django.contrib import admin

from django.contrib import admin
from .models import Job , Cc_server  , Cc_fast

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



class Cc_serverAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'server_name', 'server_cliente', 'datacenter',
        'plataforma', 'ip', 'criticidade', 'responsabilidade',
        'escalonamento1', 'escalonamento2'
    )
    list_display_links = ('id', 'server_name')
    search_fields = ('server_name', 'server_cliente', 'ip')  # Campos que podem ser buscados
    list_filter = ('datacenter', 'plataforma', 'criticidade')  # Campos para filtragem
    ordering = ('server_name',)  # Ordenação padrão

admin.site.register(Cc_server, Cc_serverAdmin)


from django.contrib import admin
from .models import Cc_fast

class CcFastAdmin(admin.ModelAdmin):
    list_display = ('server_name', 'server_cliente', 'datacenter', 'ip', 'criticidade')
    search_fields = ('server_name', 'server_cliente', 'datacenter', 'ip')
    list_filter = ('plataforma', 'criticidade', 'responsabilidade')

admin.site.register(Cc_fast, CcFastAdmin)
