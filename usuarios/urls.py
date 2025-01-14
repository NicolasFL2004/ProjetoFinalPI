from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.perfil_edit, name='perfil_edit'),
]