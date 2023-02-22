from django.urls import path

from . import views

urlpatterns = [
    # Principal
    path('', views.dashboard, name='home'),
]
