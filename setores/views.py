from django.shortcuts import render

# Create your views here.


def setores(request):
    context = {}
    return render(request, 'setores.html', context)
