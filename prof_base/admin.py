from django.contrib import admin
from .models import Professional_mst,Professional_Contact


@admin.register(Professional_mst)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display= ['UserName','Password','FirstName','LastName','Gender','Email','ContactNo','Qualification']
    list_editable=['FirstName','LastName','Gender','Email','ContactNo','Qualification']
    list_filter=['Gender']

@admin.register(Professional_Contact)
class ProfContact(admin.ModelAdmin):
    list_display=['FirstName','LastName','ContactNo']
    
