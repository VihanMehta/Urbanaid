from django.shortcuts import render
from prof_base.models import Professional_mst
from django.contrib import messages
def prof_login(request):
    if request.method=='POST':
        try:
            Userdetails=Professional_mst.objects.get(UserName=request.POST['uname'],Password=request.POST['psw'])
            print("Username=",Userdetails)
            request.session['UserName']=Userdetails.UserName
            return render(request,'index.html')
        except Professional_mst.DoesNotExist as e:
            messages.success(request,'Username/Password invalid..!')
    return render(request,'Prof_login.html')

def usr_logout(request):
    try:
        del request.session['UserName']
    except:
        return render(request,'index.html')
    return render(request,'index.html')

   
# Create your views here.
