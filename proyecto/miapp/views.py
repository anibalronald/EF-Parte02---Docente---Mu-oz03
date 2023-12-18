from django.shortcuts import render

def index (request):
    return render(request, 'index.html')
def crearcurso(request):
    return render(request,'crearcurso.html')
def creardocente(request):
    return render(request,'creardocente.html')
def inicio(request):
    return render(request,'inicio.html')
def integrantes(request):
    return render(request,'integrantes.html')
def listarcurso(request):
    return render(request,'listarcurso.html')
def listardocente(request):
    return render(request,'listardocente.html')
