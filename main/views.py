from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homeView(request):
    return render(request, 'main/home.html')
    # return HttpResponse(request, 'home page')