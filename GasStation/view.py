#from django.http import HttpResponse
import sys
sys.path.append("D:\jarvis\GasStation\GasStation")
# sys.path.append(".\GasStation\core")
# sys.path.append(".\core")
# sys.path.append("./core")
from django.shortcuts import render
from django.shortcuts import redirect    #导入django的重定向模块
from core.loginVerify import *

def login(request):
    #表单提交过来验证
    if request.method == "POST":    
        input_email = request.POST['user'] 
        input_pwd = request.POST['pwd']    
        if input_email == 'lei@qq.com' and input_pwd == "123":
            return redirect("http://www.baidu.com")  #重定向到百度
        else:
            return render(request, 'login.html',{'status':'ERROR Incorrect username or password'})    #如果用户输入的账号密码不对，就提示错误信息"ERROR Incorrect username or password" ，login.html页面采用模版来渲染这段错误提示
    return render(request,'login.html')
def index(request):
    context          = {}
    return render(request, 'index.html', context)
def station(request):
    context          = {}
    return render(request, 'station.html', context)