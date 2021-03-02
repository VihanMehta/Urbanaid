from django.urls import path
from .views import *
from . import views

app_name="urbanaid"

urlpatterns = [
    path('service',views.service,name='service_list'),
    path('search',views.search,name='search'),
    path('service/<slug:slug>/',servicedetailsView.as_view(),name="serviceDetail"),
    path('booking/<slug:slug>/',views.booking,name="BookingDeatils"),
    path('checkout/<slug:slug>/',views.checkout,name="checkout"),
    path('status/',views.payment_status,name="sucesss")
]
