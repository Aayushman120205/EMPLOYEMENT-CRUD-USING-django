from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'Try/LoginPage.html')

def inside(request):
    return render(request,'Try/Day1.html')

def register(request):
    return render(request,'Try/Register.html')

def delete(request):
    return render(request,'Try/Delete.html')