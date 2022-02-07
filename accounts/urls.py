from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login',views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('clients_vz', views.clients_vz, name='clients_vz'),
    path('clients_main', views.clients_main, name='clients_main')

]
