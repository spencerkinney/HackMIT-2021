from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def results(request):
    return render(request, "results.html")

def apply(request):
    return render(request, "apply.html")

def login(request):
    return render(request, "login.html")

def dashboard_add(request):
    return render(request, "dashboard_add.html")

def dashboard_edit(request):
    return render(request, "dashboard_edit.html")

def register(request):
    return render(request, "register.html")

def dashboard(request):
    return render(request, "dashboard.html")