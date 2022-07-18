from django.shortcuts import render
from .forms import RegisterForm
from .models import User

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
