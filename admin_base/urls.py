from django.urls import path
from .views import *
from . import views

app_name="urbanaid"

urlpatterns = [
    path('service',views.service,name='service_list'),
    path('search',views.search,name='search'),
    path('service/<slug:slug>/',servicedetailsView.as_view(),name="serviceDetail"),
    path('booking',views.booking),
    path('checkout',views.checkout),
]
