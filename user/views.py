from django.http import HttpResponseNotAllowed
from django.shortcuts import render, redirect
from .forms import ProfileUpdateForm, UserForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.http import JsonResponse
from django.contrib.auth.forms import PasswordChangeForm

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        bio = request.POST['bio']
        mobile = request.POST['mobile']
        
        # Validate form inputs
        if password != password_confirm:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('signup')
        
        # Save avatar if provided
        avatar = None
        if 'avatar' in request.FILES:
            avatar = request.FILES['avatar']
            fs = FileSystemStorage()
            avatar_name = fs.save(avatar.name, avatar)
            avatar_url = fs.url(avatar_name)
        else:
            avatar_url = None
        
        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.profile.bio = bio
        user.profile.mobile = mobile
        user.profile.avatar = avatar_url
        user.profile.save()
        
        messages.success(request, 'Account created successfully.')
        return redirect('login')
    
    return render(request, 'signup.html')


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
    

@login_required
def profile(request):
    profile = request.user.profile
    data ={
        'profile':profile
    }
    return render(request, 'profile.html', data)

@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        bio = request.POST.get('bio', '')
        email = request.POST.get('email', '')
        mobile = request.POST.get('mobile', '')

        # Update profile data
        profile.bio = bio
        request.user.email = email
        profile.mobile = mobile
        
        if 'avatar' in request.FILES:
            profile.avatar = request.FILES['avatar']

        # Save the changes
        profile.save()
        request.user.save()

        messages.success(request, 'Profile updated successfully.')
        return redirect('profile')

    # If it's a GET request, render the edit profile page with current data
    data = {
        'profile': profile
    }
    return render(request, 'edit_profile.html', data)

@login_required
def change_photo(request):
    profile = request.user.profile

    if request.method == 'POST' and request.FILES.get('avatar'):
        profile.avatar = request.FILES['avatar']
        profile.save()
        messages.success(request, 'Profile photo updated successfully.')
    else:
        messages.error(request, 'Failed to update profile photo.')

    return redirect('profile')

@login_required
def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if not request.user.check_password(old_password):
            messages.error(request, 'Old password is incorrect.')
        elif new_password != confirm_password:
            messages.error(request, 'New passwords do not match.')
        else:
            request.user.set_password(new_password)
            request.user.save()
            update_session_auth_hash(request, request.user)  # Important, to keep the user logged in
            messages.success(request, 'Your password has been successfully changed!')
            return redirect('profile')

    return render(request, 'change_password.html')

# @login_required
# def edit_profile(request):
#     return render(request, 'edit_profile.html')
#     user = request.user
#     profile = user.profile

#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=user)
#         profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             return redirect('profile')  # Redirect to the profile page after saving

#     else:
#         user_form = UserForm(instance=user)
#         profile_form = ProfileUpdateForm(instance=profile)

#     context = {
#         'user_form': user_form,
#         'profile_form': profile_form,
#     }
#     return render(request, 'edit_profile.html', context)
    
# @login_required
# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important to keep the user logged in
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('profile')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'change_password.html', {
#         'form': form
#     })
