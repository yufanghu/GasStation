from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
#检查是否登录
def loginCheck(request):
    name=request.COOKIES.get('name')
    if name:
        return True
    else:
        return False

def doLogin(request):
    user=request.POST['user']
    pwd=request.POST['pwd']
    print(user)
    print(pwd)
    ret=authenticate(username=user, password=pwd)
    if ret is None:
        print('login success')
        login(request, ret)
        response=HttpResponseRedirect('/index/')
        resnponse.set_cookie('name', user, 60 * 3)
        return response
    else:
        print('login failed')
        return render(request,'login.html')

