from django.urls import path
from .views import *
from . import views

app_name="urbanaid"

urlpatterns = [
    path('service',views.paginator,name='service_list'),
    path('service/<slug:slug>/',servicedetailsView.as_view(),name="serviceDetail")
]
