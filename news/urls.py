from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('sobre/', views.sobre, name='sobre'),  
    path('noticias/<int:id>/', views.detalhe_noticia, name='detalhe_noticia'),  
    path('accounts/profile/', views.perfil, name='perfil'),
    path('criar/', views.criar_noticia, name='criar_noticia'),
    path('editar/<int:id>/', views.editar_noticia, name='editar_noticia'),
    path('excluir/<int:id>/', views.excluir_noticia, name='excluir_noticia'),
    path('registrar/', views.registrar_usuario, name='register'), 
    # Adicionando URLs de autenticação
    path('accounts/', include('django.contrib.auth.urls')),  # Inclui login, logout, password_reset, etc.
    # Se quiser personalizar a URL de redefinição de senha, pode adicionar isso:
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('logout/',views.logout_view,name='logout'),
    path('logout-confirm/',views.logout_confirm,name='logout_confirm'),
    ]

