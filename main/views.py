from django.shortcuts import render
from django.http import HttpResponse

def start(request):
    return render(request, "main/index.html")
