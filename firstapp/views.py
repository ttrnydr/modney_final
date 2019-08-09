from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
def main(request):
    return render(request, 'main.html')

def apply(request):
    return render(request, 'apply.html')

def busan(request):
    return render(request, 'destination/busan.html')

def minsokchon(request):
    return render(request, 'destination/minsokchon.html')

def nami(request):
    return render(request, 'destination/nami.html')

def centralmuseum(request):
    return render(request, 'destination/centralmuseum.html')

def changdeok(request):
    return render(request, 'destination/changdeok.html')

def suncheon(request):
    return render(request, 'destination/suncheon.html')

def gbg(request):
    return render(request, 'destination/gbg.html')
    




