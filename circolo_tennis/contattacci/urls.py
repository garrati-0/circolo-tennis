from django.urls import path
from . import views

urlpatterns = [
  path('contattacci', views.contattacci, name='contattacci'),  
  path('email', views.email, name='email'), 
]