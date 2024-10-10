from django.db import models

class Servidores_CC(models.Model):
    server_name = models.CharField(max_length=255, blank=True)
    server_cliente = models.CharField(max_length=255, blank=True)
    datacenter = models.CharField(max_length=255, blank=True)
    plataforma = models.CharField(max_length=255, default='unknown', blank=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    criticidade = models.CharField(max_length=255, default='unknown', blank=True)
    responsabilidade = models.CharField(max_length=255, default='unknown', blank=True)
    storage = models.CharField(max_length=255, default='unknown', blank=True)
    os = models.CharField(max_length=255, default='unknown', blank=True)
    ambiente = models.CharField(max_length=255, default='unknown', blank=True, null=True)
    escalonamento1 = models.CharField(max_length=255, default='unknown', blank=True)
    escalonamento2 = models.CharField(max_length=255, default='unknown', blank=True)
    descricao = models.CharField(max_length=255, default='unknown', blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.server_name or "Nome não definido"

    class Meta:
        verbose_name = "Servidor CC"
        verbose_name_plural = "Servidores CC"  


class Servidores_FastShop(models.Model):
    server_name = models.CharField(max_length=255, blank=True)
    server_cliente = models.CharField(max_length=255, blank=True)
    datacenter = models.CharField(max_length=255, blank=True)
    plataforma = models.CharField(max_length=255, default='unknown', blank=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    criticidade = models.CharField(max_length=255, default='unknown', blank=True)
    responsabilidade = models.CharField(max_length=255, default='unknown', blank=True)
    storage = models.CharField(max_length=255, default='unknown', blank=True)
    os = models.CharField(max_length=255, default='unknown', blank=True)
    ambiente = models.CharField(max_length=255, default='unknown', blank=True, null=True)
    escalonamento1 = models.CharField(max_length=255, default='unknown', blank=True)
    escalonamento2 = models.CharField(max_length=255, default='unknown', blank=True)
    descricao = models.CharField(max_length=255, default='unknown', blank=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.server_name or "Nome não definido"

    class Meta:
        verbose_name = "Servidor FastShop"
        verbose_name_plural = "Servidores FastShop"  


class AccessLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user} - {self.timestamp}"