from django.shortcuts import render, HttpResponse


# Create your views here. 20221214
def index(request):
    return HttpResponse('Hello!')

