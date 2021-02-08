from django.contrib import admin
from .models import User_mst , contactus


@admin.register(User_mst)
class userAdmin(admin.ModelAdmin):
    list_display= ['UserName','Password','FirstName','LastName','Gender','Email','ContactNo']

@admin.register(contactus)
class userAdmin(admin.ModelAdmin):
    list_display= ['Name','email','Message']
    