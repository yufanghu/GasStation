def loginCheck(request):
    user=request.session.get('user')
    islogin=request.session.get('loginflag')
    if user is None or islogin is None:
        return False
    else:
        return True

def updateLoginState(request,user):
    request.session['user']=user
    request.session['loginflag']=True
    request.session.set_expiry(3)

