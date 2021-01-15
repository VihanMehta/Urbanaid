from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('index',views.index),
    path('usr_login',views.usr_login),
    path('register',views.usr_reg),
    path('logout',views.usr_logout),
    
]
