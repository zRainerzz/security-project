# filepath: /c:/Users/lenovo/Desktop/security-project/Django/login/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),  # This sets the home view as the root URL
    path('index/', views.index, name='index')  # This sets the index view as the /index URL

]