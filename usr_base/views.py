from django.shortcuts import render,redirect, HttpResponseRedirect
from usr_base.models import User_mst , contactus
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.contrib import messages
from django.views import View

def index(request):
        return render(request,'index.html')

#--------------------Registeration----------------------------
class Register(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        postData = request.POST
        UserName = postData.get('uname')
        Password = postData.get('psw')
        FirstName = postData.get('fname')
        LastName = postData.get('lname')
        Gender = postData.get('gender')
        Email = postData.get('email')
        ContactNo = postData.get('Contact')
        
        #---------------------- validation----------------------------
        value = {
            'UserName':UserName,
            'FirstName': FirstName,
            'LastName': LastName,
            'ContactNo': ContactNo,
            'Email': Email
        }

        error_message = None

        new_user = User_mst(UserName=UserName,
                            Password=Password,
                            FirstName=FirstName,
                            LastName=LastName,
                            Gender=Gender,
                            Email=Email,
                            ContactNo=ContactNo)

        error_message = self.validateCustomer(new_user)

        if not error_message:
            #print(UserName, Password, FirstName, LastName, Gender, Email, ContactNo)
            new_user.Password = make_password(new_user.Password)
            new_user.register()
            return redirect('usr_login')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'register.html', data)

    def validateCustomer(self, new_user):
        error_message = None;
        if len(new_user.UserName) < 4:
            error_message = 'UserName must be 4 char long or more'
        elif new_user.UserisExists():
            error_message = 'UserName is Already Registered..'
        elif len(new_user.FirstName) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif len(new_user.ContactNo) < 6 :
            error_message = 'Phone Number must be 10 char'
        elif len(new_user.Password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(new_user.Email) < 5:
            error_message = 'Email must be 5 char long'
        elif new_user.EmailisExists():
            error_message = 'Email Address Already Registered..'
        elif new_user.PhoneisExists():
            error_message = 'Contact Number is Already Registered..'
        elif not new_user.Gender:
            error_message = 'Please Select Gender..'
        # saving
        return error_message

#-------------------user login-------------------------

class Login(View):
    return_url = None
    def get(self , request):
        Login.return_url = request.GET.get('return_url')
        return render(request , 'login.html')

    def post(self , request):
        UserName = request.POST.get('uname')
        Password = request.POST.get('psw')
        user = User_mst.get_User_mst_by_Email(UserName)
        error_message = None
        if user:
            flag = check_password(Password, user.Password)  
            if flag:
                request.session['user'] = user.UserName
                request.session['name'] = user.FirstName +' '+ user.LastName
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('index')
            else:
                error_message = 'User name or Password invalid !!'
        else:
            error_message = 'User name or Password invalid !!'
        print(UserName, Password)
        return render(request, 'login.html', {'error': error_message})

#-------------------user log out-------------------------

def usr_logout(request):
    try:
        del request.session['user']
    except:
        return redirect('index')
    return redirect('index')

#------------------- Category -------------------------

def category(request):
    return render(request,'category.html')

#------------------- User Profile -------------------------

def profile(request):
    return render(request,'profile.html')

def update_profile(request):
    return render(request,'update-profile.html')

#------------------- Contact us -------------------------

def Contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        data = contactus(
            Name=name,
            email=email,
            Message= msg,
        )
        data.save()
        m= "we catch you soon "+ request.POST.get('name') 
        
        return render(request,'contact-us.html' , {'msg':m})
    else:
        return render(request,'contact-us.html')

#------------------- About us -------------------------
def about(request):
    return render(request,'about-us.html')

#------------ Change password ------------------------
def changpass(request):
    if request.method == 'POST':
        eror=None
        sucessmsg=None
        psw = request.POST.get('currentpass')
        newpsw = request.POST.get('newpass')
        current_usr = request.session['user']
        
        #print(current_usr)
        user=User_mst.objects.get(UserName=current_usr)
        #id=user.id
        check=check_password(psw,user.Password)
        #print(check)
        if check==True:
            user.Password = make_password(newpsw)
            user.save()
            sucessmsg=' Password Change Successfully !'
        else:
            eror='Incorrect Current Password !'
        return render(request,'update_password.html',{'eror':eror,'sucess':sucessmsg})
    else:
       return render(request,'update_password.html')

#-------------- Email Change--------------------------

def emailchange(request):
    return render(request,'update_email.html')
 