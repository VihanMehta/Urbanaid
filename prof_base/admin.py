from django.contrib import admin
from .models import Professional_Contact


@admin.register(Professional_Contact)
class ProfContact(admin.ModelAdmin):
    list_display=['FirstName','LastName','ContactNo']
    
