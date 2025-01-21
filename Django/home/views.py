# filepath: /c:/Users/lenovo/Desktop/security-project/Django/login/views.py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'index.html')



def about(request):
    return HttpResponse('''<h1>About page not configured, Does it even matter?</h1><h2>You came for the cryptic message, didn't you?</h2>''')