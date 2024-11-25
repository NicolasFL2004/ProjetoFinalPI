"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from gameinsight.views import index, novo_jogo, editar_jogo, excluir_jogo, login_view, logout_view, register
urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='cadastrar_usuario'),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('jogo/novo', novo_jogo, name='novo_jogo'),
    path('jogo/editar/<int:id>', editar_jogo, name='editar_jogo'),
    path('jogo/excluir/<int:id>', excluir_jogo, name='excluir_jogo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)