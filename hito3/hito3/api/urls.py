# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.logout_view, name='user_logout'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'), # Ajusta según tu vista de dashboard
    path('register_user/', views.register_user, name='user_register'),
    path('registration_success/<str:username>/', views.registration_success, name='registration_success'),
    path('profile/', views.profile_view, name='profile'),
    # Añade cualquier otra ruta necesaria
]
