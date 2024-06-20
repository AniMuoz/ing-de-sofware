from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.logout_view, name='user_logout'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('register_user/', views.register_user, name='user_register'),
    path('registration_success/<str:username>/', views.registration_success, name='registration_success'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/', views.profile_view, name='profile.html'),
    path('login_empresa/', views.login_empresa, name='login_empresa.html'),
    path('register_empresa/', views.register_empresa, name='register_empresa.html'),
    path('register_empresa_success/<str:username>/', views.registration_empresa_success, name='registration_empresa'),
    path('compra/', views.compra_view, name='compra'),
    path('compra/', views.compra_view, name='compra.html'),
    path('compraz/', views.compraz_view, name='compraz'),
    path('compraz/', views.compraz_view, name='compraz.html'),
]
