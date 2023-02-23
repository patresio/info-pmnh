from django.forms import ModelForm

from .models import Diretoria


class DiretoriaForm(ModelForm):
    class Meta:
        model = Diretoria
        fields = '__all__'