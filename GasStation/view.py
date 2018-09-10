#from django.http import HttpResponse
from django.shortcuts import render
 
def login(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'login.html', context)