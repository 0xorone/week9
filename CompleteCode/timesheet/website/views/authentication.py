from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from website.forms import LoginForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@csrf_exempt
@login_required(login_url='/login')
def logmeout(request):
    logout(request)
    return redirect('/login')

@csrf_exempt
def logmein(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                response = redirect("/home")
                return response
            else:
                return HttpResponse("login failed")
    else:
        form = LoginForm()
    
    return render(request, "website/login.html", {"form": form})