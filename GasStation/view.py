#from django.http import HttpResponse
from django.shortcuts import render
 
def login(request):
    # context          = {}
    # context['hello'] = 'Hello World!'
    # if request.method=='GET':
    #     return render(request, 'index.html')
    # else
    #     name=request.POST.get('user')
    #     pwd=request.POST.get('pwd')

    return render(request, 'login.html')
def index(request):
    context          = {}
    return render(request, 'index.html', context)
def station(request):
    context          = {}
    return render(request, 'station.html', context)