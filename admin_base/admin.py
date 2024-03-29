from django.contrib import admin
from .models import *
@admin.register(Category_mst)
class CategoryAdmin(admin.ModelAdmin):
     list_display= ['CategoryName','slug']
     prepopulated_fields={'slug':('CategoryName',)}

@admin.register(Service_mst)
class ProductAdmin(admin.ModelAdmin):
    list_display= ['id','ServiceName','slug','price','available','created','updated','rate']
    list_filter=['available','created','updated','rate']
    list_editable=['price','available','rate']
    prepopulated_fields={'slug':('ServiceName',)}

@admin.register(Professional_mst)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display= ['id','UserName','Password','FirstName','LastName','Gender','Email','ContactNo','Qualification']
    list_editable=['FirstName','LastName','Gender','Email','ContactNo','Qualification']
    list_filter=['Gender']

@admin.register(booking_slot)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display= ['id','order_id','ServiceName','slot','date','UserName','professional','razorpay_orderId','razorpay_payment_id','address','pincode','amount','status','payment_status']
    list_editable=['slot','date','payment_status','status']
    list_filter=['date','payment_status','status']

@admin.register(feedback_mst)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display= ['order_id','UserName','Professional','feedback']


    
