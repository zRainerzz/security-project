# filepath: /c:/Users/lenovo/Desktop/security-project/Django/login/views.py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    editors = {'name1':'Amen Allah Naamen', 'name2':'Hazem Saidani','name3': 'Ghaith Khedhri'}
    return render(request, 'home/index.html', editors)



def about(request):
    return HttpResponse('''<h1>About page not configured, Does it even matter?</h1><h2>You came for the cryptic message, didn't you?</h2>''')