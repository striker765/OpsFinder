from django.contrib import admin
from .models import Hardware, AccessLog

class HardwareAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'serial_number', 'descricao', 'local', 'status_contrato')  
    search_fields = ('marca', 'modelo', 'serial_number') 

class AccessLogAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'user')  
    search_fields = ('user',)  

admin.site.register(Hardware, HardwareAdmin)
admin.site.register(AccessLog, AccessLogAdmin)
