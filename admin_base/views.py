from django.shortcuts import render,get_list_or_404,redirect,HttpResponse
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from urbanaid import settings
from .models import *
import razorpay
razorpay_client=razorpay.Client(auth=(settings.Key_Id,settings.Key_Secret))

Time = None
Date=None
#----- paginator / page of service post---------------
def service(request):
    categories = Category_mst.objects.all()
    print(settings.Key_Id,settings.Key_Secret)
    all_post = Paginator(Service_mst.objects.filter(available = True),3) #number of post per page
    page = request.GET.get('page')
    try:
	    posts = all_post.page(page)
    except PageNotAnInteger:
	    posts = all_post.page(1)
    except EmptyPage:
	    posts = all_post.page(all_post.num_pages)
    return render(request, 'ad-list-view.html', 
                    {'posts': posts,
                     'categories':categories,
                    }) 

#----- Search service finction ---------------
def search(request):
    query=request.GET.get('query')
    posts=Service_mst.objects.filter(available = True,ServiceName__icontains=query)
    return render(request, 'service-search.html', 
                    {'posts': posts,
                    }) 
    

#---- service in details-------------------------
class servicedetailsView(TemplateView):
    template_name="single.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug=self.kwargs['slug']
        services_list= Service_mst.objects.get(slug=url_slug)
        prof=services_list.Professionalid
        data = Professional_mst.objects.get(UserName=prof)
        context['prof'] = data
        context['services_list'] = services_list
        return context
   
 #--------- Booking ---------
def booking(request,**kwargs):
            status=None
            sucess=None
            error=None
            Usr_choice=None
            url_slug=kwargs['slug']
            service= Service_mst.objects.get(slug=url_slug)
            prof=service.Professionalid
          
            print()
            if request.method=='POST':
                date=request.POST.get("date")  
                Usr_choice=request.POST.get("slot")         
                if not date:
                    error="Please select date !"
                    return render(request,"booking.html",{'service':service,'prof':prof,'error':error})
                elif not Usr_choice:
                    error="Please select Time Slot !"
                    return render(request,"booking.html",{'service':service,'prof':prof,'error':error})
                else:   
                    try:
                        book_check=booking_slot.objects.get(ServiceName=service.ServiceName,date=date,slot=Usr_choice)
                        if book_check.payment_status==1:
                            error="Sorry ! Slot is Not Available"
                            return render(request,"booking.html",{'service':service,'prof':prof,'error':error})
                        else:
                            status=True
                            global Time
                            Time=Usr_choice
                            global Date
                            Date=date
                            book=booking_slot.objects.create(UserName=User_mst.objects.get(UserName=request.session['user']),ServiceName=service.ServiceName) 
                            book.save()
                    except:
                        status=True
                        Time=Usr_choice
                        Date=date
                        book=booking_slot.objects.create(UserName=User_mst.objects.get(UserName=request.session['user']),ServiceName=service.ServiceName)
                        book.save()

                    return render(request,"booking.html",{'service':service,'prof':prof,'sucess':sucess,'error':error,'confirm_date':date,'confirm_time':Usr_choice,'status':status})       
            return render(request,"booking.html",{'service':service,'prof':prof})
        
#------- add Payment gateway--------------------


 #--------- Checkout ---------
def checkout(request,**kwargs):
    status=None
    data_save=None
    razor_id=None
    order_amount=None
    order_id=None
    add=None
    user=User_mst.objects.get(UserName=request.session['user'])
    user_id=user.id
    pincode=None
    url_slug=kwargs['slug']
    service= Service_mst.objects.get(slug=url_slug)
    prof=service.Professionalid 
    name=Professional_mst.objects.get(UserName=service.Professionalid)
    prof_name=name.UserName
    final_price=int(50+service.price)
    print(Time,Date)
    if request.method=='POST':
        add=request.POST.get("add")
        pincode=request.POST.get("pcode")
        status=True
        try:       
            book=booking_slot.objects.get(ServiceName=service.ServiceName,UserName=User_mst.objects.get(UserName=request.session['user']),razorpay_orderId=None)
        except:
            return HttpResponse("Error 505")
        book.ServiceName=service.ServiceName
        book.slot=Time
        book.date=Date
        book.amount=final_price
        book.professional=prof_name
        book.address=add
        book.pincode=pincode
        amount=final_price
        book.save()
        data_save="data successfully Save !"
        order_amount = final_price*100
        order_currency = 'INR'
        razorpay_order=razorpay_client.order.create(dict(amount=order_amount,currency=order_currency,receipt=book.order_id,payment_capture='0'))
        razor_id=razorpay_order['id']
        book.razorpay_orderId=razor_id
        book.save()
        return render(request,'checkout.html',{'service':service,'order_id':razor_id,'price':final_price,'final_price':int(final_price*100),'prof':prof,'order_amount':order_amount,'data_save':data_save,'status':status})
    return render(request,'checkout.html',{'service':service,'order_id':razor_id,'price':final_price,'final_price':int(final_price*100),'prof':prof,'order_amount':order_amount,'data_save':data_save,'status':status})


@csrf_exempt
def payment_status(request):
    if request.method=='POST':
        try:
            payment_Id=request.POST.get('razorpay_payment_id','')
            order_Id=request.POST.get('razorpay_order_id','')
            signature=request.POST.get('razorpay_signature','')
            param_dict={
                'razorpay_payment_id': payment_Id,
                'razorpay_order_id':order_Id,
                'razorpay_signature':signature
            }
            try:
                order_db=booking_slot.objects.get(razorpay_orderId=order_Id) 
            except:
                return render(request,"book-fail.html")
            order_db.razorpay_payment_id=payment_Id
            order_db.booked=True
            order_db.save()
            result=razorpay_client.utility.verify_payment_signature(param_dict)   
            if result==None:
                amount=order_db.amount*100
                try:
                    razorpay_client.payment.capture(payment_Id,amount)
                    order_db.payment_status=1
                    order_db.save()
                    return render(request,"book-sucess.html")
                except:
                    order_db.payment_status=2
                    order_db.save()
                    return render(request,"book-fail.html") 
            else:
                order_db.payment_status=2
                order_db.save()
                return render(request,"book-fail.html")
        except:
            return render(request,"book-fail.html")
    return render(request,"book-sucess.html")
