from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.db import models
from GasStation.models import *

def loadWarningData(request):
    warning=tbl_warning.objects.all()
    return render(request, 'index.html', {"warning":warning})
    

