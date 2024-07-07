from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .forms import SignUpForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            profile = Profile.objects.create(
                user=user,
                bio=form.cleaned_data['bio'],
                mobile=form.cleaned_data['mobile'],
                avatar=form.cleaned_data['avatar']
            )

            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password.')
    
    
    return render(request, 'login.html')  



def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login') 
    else:
        return HttpResponseNotAllowed(['POST'])

