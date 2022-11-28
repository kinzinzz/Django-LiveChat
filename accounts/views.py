from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    
    return render(request, 'accounts/index.html')


def create(request):
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:index')
        
    else:
        form = CustomUserCreationForm()
    context = {
        'form':form
    }
    
    return render(request, 'accounts/create.html', context)

def user_login(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("accounts:index")

    else:
        form = AuthenticationForm()

    return render(request, "accounts/login.html", {"form": form})