from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class Contrato(models.Model):
    n_contrato = models.CharField('Número do contrato', max_length=100, primary_key=True)
    descricao = models.CharField('Descrição', max_length=250)
    empresa = models.CharField('Empresa', unique=True, max_length=250)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)
    slug = AutoSlugField(unique=True, always_update=True, populate_from="n_contrato")
    def __str__(self):
        return self.n_contrato + ' - ' + self.empresa

class Componente(models.Model):
    n_contrato = models.ForeignKey('Planejamento.Contrato', verbose_name='Contrato', on_delete=models.CASCADE)
    desenho = models.CharField('Nº desenho', max_length=250)
    material_de_origem = models.CharField('Material de origem', max_length=250, blank=True, null=True)
    item = models.CharField('Item', max_length=250)
    tag = models.CharField('Tag', max_length=250)
    area = models.DecimalField('Área (m²)', decimal_places=2, max_digits=8,blank=True, null=True)
    massa = models.DecimalField('Massa (kg)', decimal_places=2, max_digits=8,  blank=True, null=True)
    n_romaneio = models.IntegerField('Nº Romaneio',  blank=True, null=True)
    obs = models.CharField('Observação', max_length=250, blank=True, null=True)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.tag + ' _ ' + self.desenho
