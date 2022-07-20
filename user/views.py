from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from .models import User


def home(request):
    return render(request, 'user/home.html')

@login_required
def dashboard(request):
    return render(request, 'user/dashboard.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            User.objects.create(user=user)

            return render(request, 'user/register_done.html', {'user': user})
    else:
        form = RegisterForm()
    
    return render(request, 'user/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(request,
                                username=form.cleaned_data['username'],
                                password=form.cleaned_data['password']
                                )
                                
            if user is not None:
                if user.is_active:
                    auth_login(request, user)

                    return redirect('user:dashboard')
                else:
                    return redirect('user:home')
        else:
            return render(request, 'user/login.html', {'form': form})
    else:
        form = LoginForm()

    return render(request, 'user/login.html', {'form': form})

@login_required
def logout(request):
    auth_logout(request)
    return redirect('user:home')
