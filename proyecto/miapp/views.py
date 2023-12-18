from django.shortcuts import render, redirect,HttpResponse
from miapp.models import Docente
from django.contrib import messages
def index (request):
    return render(request, 'index.html')
def crearcurso(request):
    return render(request,'crearcurso.html')
def creardocente(request):
    return render(request,'creardocente.html')
def guardardocente(request):
    if request.method == 'POST':
        codigo=request.POST['codigo']
        nombre=request.POST['nombre']
        apellido_paterno=request.POST['apellido_paterno']
        apellido_materno=request.POST['apellido_materno']
        dni=request.POST['dni']
        fecha_nac=request.POST['fecha_nac']
        estado=request.POST['estado']
    else:
        return HttpResponse("<h2>No se ha podido resgitrar el docente</h2>")
    docente=Docente(
        codigo=codigo,
        nombre=nombre,
        apellido_paterno=apellido_paterno,
        apellido_materno=apellido_materno,
        dni=dni,
        fecha_nac=fecha_nac,
        estado=estado
    )
    docente.save()
    messages.success(f"<h2>No se ha podido resgitrar el docente: {docente.nombre}</h2>")
    return redirect('/listardocente')
def eliminar(request,id):
    docente=Docente.objects.get(pk=id)
    docente.delete()
    return redirect('/listardocente')
def inicio(request):
    return render(request,'inicio.html')
def integrantes(request):
    return render(request,'integrantes.html')
def listarcurso(request):
    return render(request,'listarcurso.html')
def listardocente(request):
    docente=Docente.objects.all()
    return render(request,'listardocente.html',{
        'titulo': 'LISTA DE DOCENTES',
        'docentes':docente
    })
