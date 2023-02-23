from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.views import View
from django.db import transaction

from .models import Diretoria, Setor

# Diretoria
class DiretoriaList(ListView):
    model = Diretoria
    context_object_name = 'diretorias'
    template_name = 'diretorias.html'

class DiretoriaCreate(CreateView):
    model = Diretoria
    fields = ['nome']
    template_name = 'diretoria_form.html'
    success_url = reverse_lazy('diretorias')

class DiretoriaUpdate(UpdateView):
    model = Diretoria
    fields = ['nome']
    template_name = 'diretoria_form.html'
    success_url = reverse_lazy('diretorias')

class DiretoriaDelete(DeleteView):
    model = Diretoria
    context_object_name = 'diretoria'
    template_name = 'diretoria_confirm_delete.html'
    success_url = reverse_lazy('diretorias')


#Setores

class SetorList(ListView):
    model = Setor
    context_object_name = 'setores'
    template_name = 'setores.html'

class SetorCreate(CreateView):
    model = Setor
    fields = '__all__'
    template_name = 'setor_form.html'
    success_url = reverse_lazy('setores')

class SetorUpdate(UpdateView):
    model = Setor
    fields = '__all__'
    template_name = 'setor_form.html'
    success_url = reverse_lazy('setores')

class SetorDelete(DeleteView):
    model = Setor
    context_object_name = 'setor'
    template_name = 'setor_confirm_delete.html'
    success_url = reverse_lazy('setores')