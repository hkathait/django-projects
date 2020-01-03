from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.register, name='register'),
    path('sent/', views.activation_sent_view, name="activation_sent_view"),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='course'), name='logout'),
    path('forgot', views.forgot, name='forgot')

]
