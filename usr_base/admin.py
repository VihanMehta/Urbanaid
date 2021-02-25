from django.contrib import admin
from .models import User_mst , contactus


@admin.register(User_mst)
class userAdmin(admin.ModelAdmin):
    list_display= ['id','UserName','Password','FirstName','LastName','Gender','Email','ContactNo','address','Postcode']
    list_editable=['address','Postcode']
    
@admin.register(contactus)
class userAdmin(admin.ModelAdmin):
    list_display= ['Name','email','Message']
    