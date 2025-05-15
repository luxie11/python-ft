from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagrindinis, name='pagrindinis'),
    path('new/', views.new_post, name='new_post'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
]