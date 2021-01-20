from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.index, ),
    path('usr_login',Login.as_view()),
    path('register', Register.as_view(), name='Register'),
    path('logout',views.usr_logout),
]
