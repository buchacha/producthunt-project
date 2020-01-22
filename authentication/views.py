from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    
    if request.method == 'POST':
        # Then user want to sign up and entered all fields
        
        if request.POST['password'] == request.POST['confirmPassword']:
            
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'authentication/signup.html', {'error':'Username has already been taken'})
            
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'authentication/signup.html', {'error':'Password must match'})
            
    else:
        # Then user want to open page to enter info
        return render(request, 'authentication/signup.html')

def login(request):
    if request.method == 'POST':
        # Then user want to log in and entered all fields
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'authentication/login.html', {'error':'username or password is incorrect'})
    else:
        # Then user want to open page to enter info
        return render(request, 'authentication/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')