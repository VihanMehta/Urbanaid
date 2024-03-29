from django.urls import path
from .views import *

from . import views

urlpatterns = [ 
    path('',views.index,name='main'),
    path('index',views.index,name='index' ),
    path('usr_login',Login.as_view(),name='login'),
    path('register', Register.as_view(), name='Register'),
    path('logout',views.usr_logout),
    path('profile',views.profile),
    path('update_profile',views.update_profile),
    path('contactUs',views.Contact),
    path('aboutUs',views.about),
    path('change_pass',views.changpass),
    path('change_email',views.emailchange),
    path('history',views.history),
    path('generateinvoice/<str:order_id>/', GenerateInvoice.as_view(), name = 'generateinvoice'),
    path('password-reset/',views.passreset),
   
]
