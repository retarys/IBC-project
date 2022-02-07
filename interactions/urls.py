from django.urls import path
from . import views


urlpatterns = [
    path('snippet/', views.snippet_detail, name="snippet"),
    path('form/', views.form, name="form"),
]
