from django.db import models

from django.urls import reverse
from django.utils import timezone
from django.db.models import Q


class Professional_mst(models.Model):
    UserName = models.CharField(max_length=10, null=False, unique=True)
    Password = models.CharField(max_length=15, null=False)
    FirstName = models.CharField(max_length=10, null=False)
    LastName = models.CharField(max_length=10, null=False)
    Gender = models.CharField(max_length=1, null=False)
    Email = models.CharField(max_length=30, null=False, unique=True)
    ContactNo = models.CharField(max_length=10, null=False, unique=True)
    Qualification = models.CharField(max_length=50, null=False)

    def __str__(self):
        return (self.UserName)

    @staticmethod
    def get_prof_mst_by_username(UserName):
        try:
            return Professional_mst.objects.get(UserName=UserName)
        except:
            return False
    
class Category_mst(models.Model):
    CategoryName = models.CharField(max_length=25, db_index=True ,null=False)
    slug= models.SlugField(max_length=200,unique=True)
    
    def __str__(self):
        return self.CategoryName

rate_choice=(
       ('1','1'),
       ('2','2'),
       ('3','3'),
       ('4','4'),
       ('5','5'),
   )

class Service_mst(models.Model):
    Categoryid = models.ForeignKey('Category_mst', max_length=7, on_delete=models.CASCADE)
    Professionalid = models.ForeignKey('Professional_mst', max_length=5, on_delete=models.CASCADE)
    ServiceName=models.CharField(max_length=355, db_index=True)
    slug= models.SlugField(max_length=455,unique=True)
    image=models.ImageField(upload_to='services/%Y/%m/%d', blank = True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    rate=models.CharField(choices=rate_choice ,max_length=5 , blank=True)

    def __str__(self):
        return self.ServiceName


class booking_slot(models.Model):
    order_status=(
        (1,'PENDING'),
        (2,'ACCEPTED'),
        (3,'DECLINED'),
        (4,'COMPLETE'),
   )

    payment_status_choices = (
        (1, 'SUCCESS'),
        (2, 'FAILURE' ),
        (3, 'PENDING'),
    )
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True, default=None)
    ServiceName=models.CharField(max_length=255 ,null=True, blank=True)
    slot=models.CharField(max_length=255 ,null=True, blank=True)
    date=models.CharField(max_length=60, null=True, blank=True)
    user=models.CharField(max_length=60, null=True, blank=True)
    datetime_of_payment = models.DateTimeField(default=timezone.now)
    professional=models.CharField(max_length=60, null=True, blank=True)
    razorpay_orderId=models.CharField(max_length=255 ,null=True, blank=True)
    razorpay_payment_id=models.CharField(max_length=155 ,null=True, blank=True)
    address=models.CharField(max_length=600, null=True, blank=True)
    pincode=models.CharField(max_length=10, null=True, blank=True)
    amount=models.IntegerField(null=True, blank=True)
    status = models.IntegerField(choices = order_status, default=1)
    payment_status = models.IntegerField(choices = payment_status_choices, default=3)
    
    def __str__(self):
        return self.order_id

    def save(self, *args, **kwargs):
        if self.order_id is None and self.datetime_of_payment and self.id:
            self.order_id = self.datetime_of_payment.strftime('URBN%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)
    
    @staticmethod
    def get_order_history_data(user):
        try:
            return booking_slot.objects.filter(status=4,user=user,payment_status=1)
        except:
            return False
    @staticmethod
    def get_order_data(user):
        try:
            return booking_slot.objects.filter(~Q(status=4),user=user,payment_status=1)
        except:
            return False

    @staticmethod
    def get_professional_order_data(user):
        try:
            return booking_slot.objects.filter(status=1,professional=user,payment_status=1)
        except:
            return False

    @staticmethod
    def get_Accepted_orders(user):
        try:
            return booking_slot.objects.filter(status=2,professional=user,payment_status=1)
        except:
            return False

    @staticmethod
    def get_declined_orders(user):
        try:
            return booking_slot.objects.filter(status=3,professional=user,payment_status=1)
        except:
            return False
    
    @staticmethod
    def get_completed_orders(user):
        try:
            return booking_slot.objects.filter(status=4,professional=user,payment_status=1)
        except:
            return False
            
class payment_mst(models.Model):
    order_id=models.ForeignKey('booking_slot', on_delete=models.CASCADE)
    UserName=models.CharField(max_length=155 ,null=True, blank=True)
    serviceName=models.CharField(max_length=255 ,null=True, blank=True)
    payment_id=models.CharField(max_length=155 ,null=True, blank=True)
    amount=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.payment_id
