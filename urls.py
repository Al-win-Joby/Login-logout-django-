from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name='login'),
    path('home1',views.home1,name='home1'),
    path('logout',views.logout,name=""),
    path('home',views.home,name=""),
    path('loginalogout',views.loginpageafterlogout,name="")
]