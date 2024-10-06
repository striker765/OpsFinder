from django.contrib import admin
from .models import Servidores_CC, Servidores_FastShop

def ativar_servidores(modeladmin, request, queryset):
    queryset.update(is_active=True)
    modeladmin.message_user(request, "Servidores ativados com sucesso.")

def desativar_servidores(modeladmin, request, queryset):
    queryset.update(is_active=False)
    modeladmin.message_user(request, "Servidores desativados com sucesso.")

ativar_servidores.short_description = "Ativar servidores selecionados"
desativar_servidores.short_description = "Desativar servidores selecionados"

class Servidores_CCAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'server_name', 'server_cliente', 'datacenter',
        'plataforma', 'ip', 'criticidade', 'responsabilidade',
        'escalonamento1', 'escalonamento2', 'is_active'
    )
    list_display_links = ('id', 'server_name')
    search_fields = ('server_name', 'server_cliente', 'ip') 
    list_filter = ('datacenter', 'plataforma', 'criticidade', 'is_active') 
    ordering = ('server_name',)  
    actions = [ativar_servidores, desativar_servidores]
    
    fieldsets = (
        (None, {
            'fields': ('server_name', 'server_cliente', 'ip', 'is_active')
        }),
        ('Detalhes', {
            'fields': ('datacenter', 'plataforma', 'criticidade', 'responsabilidade', 
                       'storage', 'os', 'ambiente', 'escalonamento1', 'escalonamento2', 'descricao')
        }),
    )

admin.site.register(Servidores_CC, Servidores_CCAdmin)

class Servidores_FastShopAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'server_name', 'server_cliente', 'datacenter',
        'plataforma', 'ip', 'criticidade', 'responsabilidade', 
        'escalonamento1', 'escalonamento2', 'is_active'
    )
    list_display_links = ('id', 'server_name')
    search_fields = ('server_name', 'server_cliente', 'datacenter', 'ip')
    list_filter = ('plataforma', 'criticidade', 'responsabilidade', 'is_active')  
    actions = [ativar_servidores, desativar_servidores]
    
    fieldsets = (
        (None, {
            'fields': ('server_name', 'server_cliente', 'ip', 'is_active')
        }),
        ('Detalhes', {
            'fields': ('datacenter', 'plataforma', 'criticidade', 'responsabilidade', 
                       'storage', 'os', 'ambiente', 'escalonamento1', 'escalonamento2', 'descricao')
        }),
    )

admin.site.register(Servidores_FastShop, Servidores_FastShopAdmin)
