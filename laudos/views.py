from django.shortcuts import render


from .models import *
# Create your views here.


def home(request):
    context = {}
    return render(request, 'laudos/dashboard.html', context)


# Diretorias
def setores(request):
    diretorias = Diretoria.objects.all()
    setores = Setor.objects.all()
    context = {
        'diretorias': diretorias,
        'setores': setores
    }
    return render(request, 'laudos/setores.html', context)
