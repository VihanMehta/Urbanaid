from django.urls import path
from . import views

urlpatterns = [
    path('login',views.prof_login,name="proflogin"),
    path('logout',views.prof_logout),
    path('profile',views.profile_set),
    path('changepass',views.changepass),
    path('reviews',views.review),
    path('',views.dashbord,name="dashbord"),
]
