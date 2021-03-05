from django.shortcuts import render,redirect
from admin_base.models import Professional_mst
from django.contrib import messages
from usr_base.models import User_mst
from admin_base.models import booking_slot,feedback_mst
from django.contrib.sessions.models import Session

def prof_login(request):
    error_msg=None
    if request.method=='POST':
                UserName = request.POST.get('uname')
                Password = request.POST.get('psw')
                try:
                    match=Professional_mst.objects.get(UserName=UserName)
                except:
                    return render(request,"Prof_login.html",{'error':error_msg})
                ps=match.Password
                if ps==Password:
                        request.session['professional']=UserName
                        request.session['profname']=match.FirstName+' '+match.LastName
                        request.session['proffname']=match.FirstName
                        request.session['proflname']=match.LastName
                        request.session['profemail']=match.Email
                        request.session['profphone']=match.ContactNo
                        request.session['profgender']=match.Gender
                        request.session['profqulifiaction']=match.Qualification
                        request.session['profadd']=match.address
                        request.session['profpcode']=match.Postcode
                        return redirect("dashbord")
                else:
                        error_msg="Enter Valid Password !"
                        return render(request,"Prof_login.html",{'error':error_msg})
    return render(request,"Prof_login.html",{'error':error_msg})
            
        

def prof_logout(request):
    try:
        del request.session['professional']
        del request.session['profname']
    except:
        return redirect('proflogin')
    return redirect('proflogin')

#------- dashboard-------
def dashbord(request):
    try:
        if request.session['professional']:
            prof=request.session['professional']
            orders=booking_slot.get_professional_order_data(prof)
            accepted_orders=booking_slot.get_Accepted_orders(prof)
            declined_orders=booking_slot.get_declined_orders(prof)
            if request.method=='POST':
                order_id=request.POST.get('order_id')
                change_status=request.POST.get('status')
                try:
                    change=booking_slot.objects.get(order_id=order_id)
                except:
                    return render(request,"Profesional-dashboard.html",{'orders':orders,'accepted_orders':accepted_orders,'declined_orders':declined_orders})
                change.status=change_status
                change.save()
            return render(request,"Profesional-dashboard.html",{'orders':orders,'accepted_orders':accepted_orders,'declined_orders':declined_orders})
    except:
        return redirect('proflogin')
    return redirect('proflogin')


#----- History---------------
def history(request):
    try:
        if request.session['professional']:
            prof=request.session['professional']
            orders=booking_slot.get_completed_orders(prof)
            return render(request,"prof_history.html",{'orders':orders})
    except:
        return redirect('proflogin')
    return render(request,"prof_history.html",{'orders':orders})


#-------- profile------------------
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
    return render(request,"professional-profile-settings.html",{'msg':msg})

#------- Reviews-----------------
def review(request):
    try:
        if request.session['professional']:
            feedback_data=feedback_mst.get_data_by_professional(Professional_mst.objects.get(UserName=request.session['professional']))
            print(feedback_data)
            return render(request,"reviews.html",{'feedback_data':feedback_data})

    except:
       return redirect("proflogin")

#---
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