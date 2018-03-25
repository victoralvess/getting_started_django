from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Hello World. This is the polls index.")

def say_hello(request, name):
	return HttpResponse('Hello {}. Welcome to this route.'.format(name))

def say_goodbye(request, name):
	return HttpResponse('Goodbye ' + name)