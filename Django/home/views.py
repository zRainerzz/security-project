# filepath: /c:/Users/lenovo/Desktop/security-project/Django/login/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DataForm
# Create your views here.

def home(request):
    editors = {'name1': 'amen allah naamen', 'name2': 'hazem saidani', 'name3': 'ghaith khedhri'}
    return render(request, 'home/index.html', editors)

# New view for handling the form submission
def index(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the same page after saving
    else:
        form = DataForm()
    return render(request, 'home/index.html', {'form': form})
