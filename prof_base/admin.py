from django.contrib import admin
from .models import Professional_mst,Professional_Contact


@admin.register(Professional_mst)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display= ['UserName','Password','FirstName','LastName','Gender','Email','ContactNo','Qualification','address','Postcode']
    list_editable= ['FirstName','LastName','Gender','Email','ContactNo','Qualification','address','Postcode']
    list_filter=['Gender','Qualification']

@admin.register(Professional_Contact)
class ProfContact(admin.ModelAdmin):
    list_display=['FirstName','LastName','ContactNo']
    
