from django.shortcuts import render,redirect
from prof_base.models import Professional_mst
from django.contrib import messages
from django.contrib.sessions.models import Session

def prof_login(request):
    error_msg=None
    if request.method=='POST':
        UserName = request.POST.get('uname')
        Password = request.POST.get('psw')
        try:
            match=Professional_mst.objects.get(UserName=UserName)
            ps=match.Password
            if ps==Password:
                request.session['professional']=UserName
                request.session['profname']=match.FirstName+' '+match.LastName
                request.session['profqulifiaction']=match.Qualification
                return redirect("dashbord")
            else:
                error_msg="Enter Valid Password !"
                return render(request,"Prof_login.html",{'error':error_msg})
        except:
            error_msg="Invalid Username & Password ! "
            return render(request,"Prof_login.html",{'error':error_msg})
    return render(request,"Prof_login.html",{'error':error_msg})        
        

def prof_logout(request):
    try:
        del request.session['professional']
        del request.session['profname']
    except:
        return redirect('proflogin')
    return redirect('proflogin')

def dashbord(request):
    try:
        if request.session['professional']:
            return render(request,"Profesional-dashboard.html")
    except:
        return redirect("proflogin")

def profile_set(request):
    try:
        if request.session['professional']:
            return render(request,"professional-profile-settings.html")
    except:
        return redirect("proflogin")

