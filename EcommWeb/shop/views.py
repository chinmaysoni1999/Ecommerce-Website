from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def shopHome(request):
    return render(request,'shop/index.html')

