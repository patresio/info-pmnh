from django.shortcuts import render, redirect


from .models import *
from .forms import DiretoriaForm, SetorForm
# Create your views here.


def home(request):
    context = {}
    return render(request, 'laudos/dashboard.html', context)


# Diretorias
def setores(request):
    diretorias = Diretoria.objects.all()
    form_diretoria = DiretoriaForm()
    setores = Setor.objects.all()
    # form_setor = SetorForm()
    context = {
        'diretorias': diretorias,
        'setores': setores,
        # 'form_setor': form_setor,
        'form_diretoria': form_diretoria
    }
    return render(request, 'laudos/setores.html', context)


def createDiretoria(request):
    if request.method == 'POST':
        nome = request.POST.get('diretoria_nome')

        diretoria = Diretoria(
            nome=nome,
        )

        diretoria.save()

        return redirect('setores')


def createSetor(request):
    if request.method == 'POST':
        nome = request.POST.get('nome_setor')
        responsavel = request.POST.get('responsavel_setor')
        diretoria = request.POST.get('diretoria_setor')

        setor = Setor(
            diretoria_id=diretoria,
            nome=nome,
            responsavel=responsavel,
        )

        setor.save()

        return redirect('setores')
