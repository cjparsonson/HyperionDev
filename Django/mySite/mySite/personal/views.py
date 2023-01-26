from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "index.html")


def cv(request):
    return render(request, "cv.html")


def coding(request):
    return render(request, "coding.html")
