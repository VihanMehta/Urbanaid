from django.shortcuts import render,redirect
from prof_base.models import Professional_mst
from django.contrib import messages
from django.contrib.sessions.models import Session

def prof_login(request):
    error_msg=None
    try:
        if request.session['professional']:
            return redirect("dashbord")  
    except:
        if request.method=='POST':
                UserName = request.POST.get('uname')
                Password = request.POST.get('psw')
                try:
                    match=Professional_mst.objects.get(UserName=UserName)
                    ps=match.Password
                    if ps==Password:
                        request.session['professional']=UserName
                        request.session['profname']=match.FirstName+' '+match.LastName
                        request.session['proffname']=match.FirstName
                        request.session['proflname']=match.LastName
                        request.session['profemail']=match.Email
                        request.session['profphone']=match.ContactNo
                        request.session['profqulifiaction']=match.Qualification
                        request.session['profadd']=match.address
                        request.session['profpcode']=match.Postcode
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
    msg=None
    try:
        if request.session['professional']:
            if request.method=='POST':
                usr=request.session['professional']  
                user=Professional_mst.objects.get(UserName=usr)
                if request.POST.get('address'):
                    address = request.POST.get('address') 
                    user.address=address
                if request.POST.get('pcode'):
                    pcode = request.POST.get('pcode')  
                    user.Postcode=pcode

                user.save()
                msg=" Data added sucessfully! "
                return render(request,"professional-profile-settings.html",{'msg':msg})
            else:
                return render(request,"professional-profile-settings.html",{'msg':msg})
    except:
        return redirect("proflogin")

#------- Reviews-----------------
def review(request):
    try:
        if request.session['professional']:
            return render(request,"reviews.html")
    except:
        return redirect("proflogin")

def changepass(request):
    error=None
    sucess=None
    try:
        if request.session['professional']:
            if request.method=='POST':
                curpass=request.POST.get("currentpass")
                newpass=request.POST.get("newpass")
                login_usr=request.session['professional']
                usr=Professional_mst.objects.get(UserName=login_usr)
                if curpass==usr.Password:
                    usr.Password=newpass
                    usr.save()
                    sucess="Hurrey ! Password Successfully Changed !"
                else:
                    error="Enter valid Current Password !"
                    return render(request,"Prof-change-password.html",{'error':error,'sucess':sucess})
            return render(request,"Prof-change-password.html",{'error':error,'sucess':sucess})
    except:
        return redirect("proflogin")
    return render(request,"Prof-change-password.html",{'error':error,'sucess':sucess})