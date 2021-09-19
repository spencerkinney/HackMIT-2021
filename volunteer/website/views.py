from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserCreationForm2
from .models import Post


def home(request):
    return render(request, "home.html")

def results(request):
    posts = Post.objects.all().order_by('-lastModified')
    context = {
        "posts": posts,
    }
    return render(request, "results.html", context)

def apply(request):
    return render(request, "apply.html")

def registerUser(request):
    if request.method == 'POST':
        form = UserCreationForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect(dashboard)
    else:
        form = UserCreationForm2()
    return render(request, "register.html", {'form':form})

def loginUser(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(dashboard)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect(home)

def dashboard_add(request):
    current_user = request.user
    if current_user.is_authenticated:
        return render(request, "dashboard_add.html")
    else:
        return redirect(loginUser)

def dashboard_edit(request):
    current_user = request.user
    if current_user.is_authenticated:
        return render(request, "dashboard_edit.html")
    else:
        return redirect(loginUser)

def register(request):
    return render(request, "register.html")

def dashboard(request):
    current_user = request.user
    if current_user.is_authenticated:
        return render(request, "dashboard.html")
    else:
        return redirect(loginUser)
    