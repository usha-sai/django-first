from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index1(request):
    return HttpResponse('<h1>Hey, Welcome </h1>')
def index(request):
	return render(request, 'index.html')    
