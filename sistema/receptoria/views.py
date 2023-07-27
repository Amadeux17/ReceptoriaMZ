from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request, 'login/login.html')

#def inicio(request):
 #   return render(request, 'base.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def cobros(request):
    return render(request, 'cobros/cobros.html')

def usuarios(request):
    return render(request, 'administracion/usuarios.html')

def roles(request):
    return render(request, 'administracion/roles.html')