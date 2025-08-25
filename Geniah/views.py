from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def docente(request):
    return render(request, "docente.html")

def docente2(request):
    return render(request, "docente2.html")

def login(request):
    return render(request, "login.html")

def registro(request):
    return render(request, "registro.html")