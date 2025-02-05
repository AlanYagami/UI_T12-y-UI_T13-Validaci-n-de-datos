from django.shortcuts import render
from django.http import HttpResponse
from .utils import google_search

#from .models import Usuarios

# def index(request):
#   return HttpResponse("<h1>Hola Mundo! </h1>")


def index(request):
    return render(request, "index.html", status=200)


def error_404_view(request, exception):
    return render(request, "404.html", status=404)


def error_500_view(request, exception):
    return render(request, "500.html", status=500)


def generar_error(request):
    return 7 / 0


def onepage(request):
    return render(request, "onepage.html", status=200)


def prueba_front(request):
    # Obtener info de un formulario
    texto = request.GET.get("texto", "")

    # Vamos a generar informacion en python
    objeto1 = {
        "id": "001",
        "titulo": texto,
        "descripcion": "Texto generico 1",
    }
    objecto2 = {
        "id": "002",
        "titulo": "Segundo titulo",
        "descripcion": "Texto generico 2",
    }
    objeto3 = {
        "id": "003",
        "titulo": "Tercer titulo",
        "descripcion": "Texto generico 3",
    }

    conjunto = [objeto1, objecto2, objeto3]

    # Como mandar un objeto (variable) de python a la vista:

    # Obtener los datos de la base de datos

    #personas = Usuarios.objects.values("id", "nombres", "apellidos", "edad")
    #listaPersonas = list(personas)

    return render(
        request,
        "prueba.html",
        {"objeto": objeto1, "arreglo": conjunto},
    )


def search_view(request):
    query = request.GET.get("q", "")
    results = []
    if query:
        data = google_search(query)
        results = data.get("items", [])

    return render(request, "search.html", {"results": results, "query": query})


from django.http import JsonResponse
from .models import ErrorLog

def error_logs(request):
    return render(request, 'error_logs.html')

def get_error_logs(request):
    errors = ErrorLog.objects.values('id', 'codigo', 'mensaje', 'fecha')
    return JsonResponse({'data': list(errors)})