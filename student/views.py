from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def student(request):
    return HttpResponse('<h2>Hellow duniya </h2>')