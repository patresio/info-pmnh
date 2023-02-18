from django.forms import ModelForm
from django import forms

from .models import *


class SetorForm(ModelForm):
    class Meta:
        model = Setor
        fields = '__all__'


class DiretoriaForm(ModelForm):
    class Meta:
        model = Diretoria
        fields = '__all__'
