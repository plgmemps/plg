from django.shortcuts import render
from .models import Contrato, Componente
from .forms import ComponenteForm

def homepage(request):
    
    contratos = Contrato.objects.all()

    for i in contratos:
        print(i)
    
    context = {
        'contratos' : contratos,
    }
    return render(request, 'planejamento/homepage.html', context)
def obra(request, slug):
    
    obra = Contrato.objects.filter(slug=slug)
    for field in obra:
       n_contrato =field.n_contrato
    
    componentes = Componente.objects.filter(n_contrato=n_contrato)
    form = ComponenteForm(request.POST)


    context = {
        'obra':obra,
        'componentes':componentes,
        'form':form,
    }
    
    return render(request, 'planejamento/obra.html', context)