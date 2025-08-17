from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Home page (only for logged-in users)
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

# Login
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            # Invalid credentials, stay on login page
            return render(request, 'login.html', {"error": "Invalid username or password"})

    return render(request, 'login.html')

# Logout
def logoutUser(request):
    logout(request)
    return redirect("/login")
