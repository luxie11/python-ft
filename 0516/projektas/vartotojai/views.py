from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect("login")
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    return render(request, 'index.html')

@login_required
def secret(request):
    return render(request, 'secured.html')

@login_required
def profile(request):
    return render(request, 'profile.html')