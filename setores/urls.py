from django.urls import path

from . import views


urlpatterns = [
    path('', views.setores, name='setores'),
]
