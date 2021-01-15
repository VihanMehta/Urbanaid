from django.shortcuts import render
from usr_base.models import User_mst
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def usr_reg(request):
    if request.method=='POST':
        model=User_mst()
        model.UserName=request.POST['uname']
        model.Password=request.POST['psw']
        model.FirstName=request.POST['fname']
        model.LastName=request.POST['lname']
        model.Gender=request.POST['gender']
        model.Email=request.POST['email']
        model.ContactNo=request.POST['Contact']
        model.save()
        messages.success(request,'Success fully Register ! '+request.POST['uname'])
        return render(request,'register.html')
    else:
        return render(request,'register.html')

def usr_login(request):
    if request.method=='POST':
        try:
            Userdetails=User_mst.objects.get(UserName=request.POST['uname'],Password=request.POST['psw'])
            print("Username=",Userdetails)
            request.session['UserName']=Userdetails.UserName
            return render(request,'index.html')
        except User_mst.DoesNotExist as e:
            messages.success(request,'Username/Password invalid..!')
    return render(request,'login.html')

def usr_logout(request):
    try:
        del request.session['UserName']
    except:
        return render(request,'index.html')
    return render(request,'index.html')

def category(request):
    return render(request,'category.html')

# Create your views here.
