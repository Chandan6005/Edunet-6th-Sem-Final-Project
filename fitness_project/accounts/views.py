from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.decorators import login_required

def auth_view(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            age = request.POST['age']
            gender = request.POST['gender']
            height = request.POST['height']
            weight = request.POST['weight']
            goal = request.POST['goal']

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            profile = user.profile
            profile.age = age
            profile.gender = gender
            profile.height = height
            profile.weight = weight
            profile.goal = goal
            profile.save()

            login(request, user)
            return redirect('dashboard')
        
        elif 'login'in request.POST:
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username,password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
            
    return render(request, 'login_register.html')

@login_required
def profile_view(request):
    profile = request.user.profile

    if request.method == 'POST':
        profile.age = request.POST['age']
        profile.gender = request.POST['gender']
        profile.height = request.POST['height']
        profile.weight = request.POST['weight']
        profile.goal = request.POST['goal']
        profile.save()

    return render(request, 'profile.html', {'profile': profile})

def logout_view(request):
    logout(request)
    return redirect('auth')