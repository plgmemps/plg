from django.contrib import admin
from .models import Contrato, Componente

class ComponenteInline(admin.TabularInline):
    model = Componente

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display=['n_contrato','empresa','descricao']
    inlines=[ComponenteInline]

# admin.site.register(Contrato)
admin.site.register(Componente)
