from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hola, mundo. Esta es la página de inicio de nombreapp.")


