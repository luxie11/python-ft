from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def pagrindinis(request):
    context = {
        'pavadinimas': "Mano pagrindinis",
        'antraste': "Mano Antraste",
    }
    return render(request, 'pagrindinis.html', context)

def apie(request):
    return render(request, 'apie.html')