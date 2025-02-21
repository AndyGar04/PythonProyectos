from django.shortcuts import render

# Create your views here.
def index(request):
    contexto = {"mensaje":"Bienvenidos a mi aplicación en Django."}
    return render(request, "myapp/index.html", contexto)

def saludo(request, nombre):
    saludito = {"mensaje": f"Bienvenid@ {nombre} a mi aplicación en Django."}
    return render(request, "myapp/index.html", saludito)
