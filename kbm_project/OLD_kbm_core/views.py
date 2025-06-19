#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Selamat datang di Aplikasi Pengelolaan KBM </h1><p>Tekno Multi Kreasi Project</p>")
