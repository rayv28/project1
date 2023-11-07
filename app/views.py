from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def fun(request):
  return HttpResponse('this is a function in views')
