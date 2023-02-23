from django.urls import path

from .views import DiretoriaList, SetorList, DiretoriaCreate, DiretoriaUpdate, DiretoriaDelete, SetorCreate, SetorDelete, SetorUpdate


urlpatterns = [
    #Diretoria
    path('diretorias/', DiretoriaList.as_view(), name='diretorias'),
    path('add-diretoria/', DiretoriaCreate.as_view(), name='add-diretoria'),
    path('edit-diretoria/<int:pk>/', DiretoriaUpdate.as_view(), name='edit-diretoria'),
    path('delete-diretoria/<int:pk>/', DiretoriaDelete.as_view(), name='delete-diretoria'),
    #Setor
    path('', SetorList.as_view(), name='setores'),
    path('add-setor/', SetorCreate.as_view(), name='add-setor'),
    path('edit-setor/<int:pk>/', SetorUpdate.as_view(), name='edit-setor'),
    path('delete-setor/<int:pk>/', SetorDelete.as_view(), name='delete-setor'),
]
