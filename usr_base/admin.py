from django.contrib import admin
from .models import User_mst


@admin.register(User_mst)
class userAdmin(admin.ModelAdmin):
    list_display= ['UserName','Password','FirstName','LastName','Gender','Email','ContactNo']
    