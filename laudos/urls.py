""" from django.urls import path

from . import views

urlpatterns = [
    # Principal
    path('', views.home, name='home'),
    # Diretorias Setores
    path('setores/', views.setores, name='setores'),
    path('nova_diretoria/', views.createDiretoria, name='nova_diretoria'),
    path('novo_setor/', views.createSetor, name='novo_setor'),

]
 """