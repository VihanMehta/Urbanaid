from django.contrib import admin
from .models import Category_mst,Service_mst,Professional_mst
@admin.register(Category_mst)
class CategoryAdmin(admin.ModelAdmin):
     list_display= ['CategoryName','slug']
     prepopulated_fields={'slug':('CategoryName',)}

@admin.register(Service_mst)
class ProductAdmin(admin.ModelAdmin):
    list_display= ['ServiceName','slug','price','available','created','updated']
    list_filter=['available','created','updated']
    list_editable=['price','available']
    prepopulated_fields={'slug':('ServiceName',)}

@admin.register(Professional_mst)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display= ['UserName','Password','FirstName','LastName','Gender','Email','ContactNo','Qualification']
    list_editable=['FirstName','LastName','Gender','Email','ContactNo','Qualification']
    list_filter=['Gender']

