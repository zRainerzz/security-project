from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),  # This sets the login view as the root URL

]