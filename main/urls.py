from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from gameinsight.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path("avaliacoes/", include(("gameinsight.urls", "gameinsight"), namespace="avaliacoes")),
    path("jogos/", include(("jogos.urls", "jogos"), namespace="jogos")),
    path('accounts/', include(('usuarios.urls', 'usuarios'), namespace='usuarios')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)