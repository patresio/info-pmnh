from django.urls import path

from . import views

urlpatterns = [
    # Principal
    path('', views.home, name='home'),
    # Diretorias
    path('setores/', views.setores, name='setores'),
    # Setores
]
