from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='home_page'),  # This sets the login view as the root URL

]