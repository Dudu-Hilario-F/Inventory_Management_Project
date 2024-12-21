from django.shortcuts import render
from django.http import Http404, HttpResponse


def paginaTeste(request):
    return render(request, "global/index.html")


def home(request):
    return HttpResponse("Ola")