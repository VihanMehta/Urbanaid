from django.shortcuts import render,redirect, HttpResponseRedirect
from usr_base.models import User_mst , contactus
from django.views.generic import TemplateView
from admin_base.models import booking_slot

from django.contrib.auth.hashers import make_password,check_password
from django.contrib.sessions.models import Session
from django.views import View

curt_usr=None

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
            msg=" You are sucessfully Registered !"
            return render(request, 'register.html', {'sucess':msg})
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'register.html', data)

    def validateCustomer(self, new_user):
        error_message = None
        if len(new_user.UserName) < 4:
            error_message = 'UserName must be 4 char long or more'
        elif new_user.UserisExists():
            error_message = 'sorry ! UserName is Already in system ! Try another..'
        elif len(new_user.FirstName) < 2:
            error_message = 'First Name must be 2 char long or more'
        elif (len(new_user.ContactNo)!=10 ):
            error_message = 'Phone Number must be 10 character'
        elif len(new_user.Password) < 6 :
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
                global curt_usr
                curt_usr=request.session['user']
                request.session['name'] = user.FirstName +' '+ user.LastName
                request.session['fname'] = user.FirstName 
                request.session['lname'] = user.LastName
                request.session['email'] = user.Email
                request.session['gender']= user.Gender
                request.session['address'] = user.address
                request.session['pcode'] = user.Postcode
                request.session['phone']=user.ContactNo
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

#------ order History--------------------
def history(request):
    user=request.session['user']
    orders=booking_slot.get_order_history_data(user)
    print(orders)
    return render(request,"orders_history.html",{'orders':orders})
#------------------- User Profile -------------------------

def profile(request):
    user=request.session['user']
    orders=booking_slot.get_order_data(user)
    print(orders)
    return render(request,"profile.html",{'orders':orders})

#------ update_profile---------------------

def update_profile(request):
    msg=None
    try:
        if request.session['user']:
            if request.method=='POST':
                usr=request.session['user']  
                user=User_mst.objects.get(UserName=usr)
                if request.POST.get('address'):
                    address = request.POST.get('address') 
                    user.address=address
                if request.POST.get('pcode'):
                    pcode = request.POST.get('pcode')  
                    user.Postcode=pcode

                user.save()
                msg=" Data added sucessfully! "
                return render(request,"update-profile.html",{'msg':msg})
            else:
                return render(request,"update-profile.html",{'msg':msg})
    except:
        return redirect("login")

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
        m= request.POST.get('name') +" ! we catch you soon : ) "
        
        return render(request,'contact-us.html' , {'msg':m})
    else:
        return render(request,'contact-us.html')

#------------------- About us -------------------------
def about(request):
    return render(request,'about-us.html')

#------------ Change password ------------------------
def changpass(request):
    eror=None
    sucessmsg=None
    try:
        if request.session['user']:
            if request.method == 'POST':
                
                psw = request.POST.get('currentpass')
                newpsw = request.POST.get('newpass')
                current_usr = request.session['user']
                user=User_mst.objects.get(UserName=current_usr)
                check=check_password(psw,user.Password)
                if check==True:
                    user.Password = make_password(newpsw)
                    user.save()
                    sucessmsg=' Password Change Successfully !'
                else:
                    eror='Incorrect Current Password !'
                    return render(request,'update_password.html',{'eror':eror,'sucess':sucessmsg})
        else:
            return render(request,'update_password.html')
    except:
        return redirect("login")
    return render(request,'update_password.html',{'error':eror,'sucess':sucessmsg})

#------ genrating pdf-----
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import os 

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)#, link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

class GenerateInvoice(View):
    def get(self, request, order_id, *args, **kwargs):
        try:
            order_db = booking_slot.objects.get(order_id = order_id, user = request.session['user'], payment_status = 1)     #you can filter using order_id as well
        except:
            return HttpResponse("505 Not Found")
        data = {
            'order_id': order_db.order_id,
            'transaction_id': order_db.razorpay_payment_id,
            'user_email': order_db.user.email,
            'date': str(order_db.datetime_of_payment),
            'name': order_db.user.name,
            'order': order_db,
            'amount': order_db.total_amount,
        }
        pdf = render_to_pdf('invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#-------------- Email Change--------------------------

def emailchange(request):
    try:
        if request.session['user']:
            if request.method=='POST':
                eror=None
                sucess=None
                cemail=request.POST['email']
                newemail=request.POST['newemail']
                # print(cemail,newemail)
                current_usr = request.session['user']
                user=User_mst.objects.get(UserName=current_usr)
                if cemail==user.Email: 
                    try:
                        match=User_mst.objects.get(Email=newemail)
                        eror='New Email is Exists in our System ! Try diffrent email'
                        return render(request,'update_email.html',{'eror':eror})          
                    except User_mst.DoesNotExist:
                        user.Email=newemail
                        user.save()
                        sucess="successfully updated new Email !"
                        return render(request,'update_email.html',{'sucess':sucess})
                else:
                    eror="Inavlid Current Email !"
                return render(request,'update_email.html',{'eror':eror,'sucess':sucess})
            else:
                return render(request,'update_email.html')
    except:
        return redirect("login")

