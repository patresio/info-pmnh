from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.urls')),
    path('setores/', include('setores.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

""" path('diretoria_setor/', include('setores.urls'), name='diretoria_setor'),
       path('laudos/', include('laudos.urls'), name='laudos'), """
