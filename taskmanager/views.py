from django.shortcuts import render
# Create your views here.

def task(request):
    return render(request, 'main.html')