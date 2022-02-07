from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('page3.html', views.page3, name='page3'),
    path('page2.html', views.page2, name='page2'),
    path('', views.home, name='home'),
    path('sotr_kompanii', views.sotr_kompanii, name='sotr_kompanii'),
    path('sotr_uroven', views.sotr_uroven,  name='sotr_uroven'),
    path('index', views.home, name='home'),
]
