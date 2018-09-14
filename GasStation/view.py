#from django.http import HttpResponse
# sys.path.append("\GasStation")
# sys.path.append(".\GasStation\core")
# sys.path.append(".\core")
# sys.path.append("./core")
from django.shortcuts import render
from django.shortcuts import redirect    #导入django的重定向模块
from GasStation.core.loginVerify import *
from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from GasStation.core.warning import *

def login(request):
    if request.method == "POST":
        user=request.POST['user']
        pwd=request.POST['pwd']
        return doLogin(request)
    else:
        #已经登录重定向到首页
        if True == loginCheck(request):
            return HttpResponseRedirect('/index')
        else:
            return render(request,'login.html')
        
def index(request):
    return loadWarningData(request)
    #return render(request, 'StationManager.html')
    
def station(request):
    context          = {}
    return render(request, 'station.html', context)