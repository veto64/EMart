from django.urls import path
from . import views
app_name='Home_Module'
urlpatterns=[
    path('',views.home,name="home"),
    path('Home/login/', views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('customer/',views.cust_api,name="cust_api"),
    path('customer/<str:name>',views.cust_api,name="cust_api")
]