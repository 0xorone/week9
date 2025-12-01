from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from website.forms.myUserForm import MyUserForm
from website.forms.createUserForm import CreateUserForm
from website.models.userDetails import UserDetails
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

@login_required(login_url='/login')
def myUser(request):
    currentUser = UserDetails.objects.get(userId=request.user.id)
    if request.method == "POST":
        form = MyUserForm(request.POST, instance=currentUser)
        if form.is_valid():
            form.save()
    else:
        form = MyUserForm(initial=vars(currentUser))

    return render(request, "website/myUser.html", {"form": form})

def createUser(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.create_user(username, email, password)   
            userDetails = UserDetails(userId=user.id, hourlyRate=5, phone='', routingNumber = '', accountNumber='')
            userDetails.save()
            login(request, user)
            return redirect("/home")
    else:
        form = CreateUserForm()

    return render(request, "website/createUser.html", {"form": form})
