from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

def splash(request):
    return render(request, 'splash.html')  # Ensure this template exists
def home(request):
    return render(request, 'home.html')  # Create home.html in templates

def index1(request):
    return render(request, 'index1.html')
def index2(request):
    return render(request, 'index2.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('dashboard')  # Change 'dashboard' to your homepage
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  # Change 'dashboard' to your homepage
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

