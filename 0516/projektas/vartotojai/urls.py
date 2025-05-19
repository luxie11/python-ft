from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/',  views.register, name='register'),
    path('accounts/login/',  LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', LogoutView.as_view(next_page="login"), name='logout'),
    path('secret/', views.secret, name='secret'),
    path('accounts/profile/', views.profile, name='profile')
]