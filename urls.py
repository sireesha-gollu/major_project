from django.urls import path
from . import views
from django.urls import include, re_path
urlpatterns=[
    path('',views.home, name='home'),
    path('adminpage',views.adminpage, name='adminpage'),
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('userpage', views.userpage, name='userpage'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    path('view_report', views.view_report, name='view_report'),
    path('button', views.button),
    path('send_email', views.send_email, name="script"),
    path('key', views.key, name='key'),
    path('about', views.about, name='about'),
    path('contactus', views.contactus, name='contactus'),
    path('view_data', views.view_data, name="view_data"),
    path('view', views.view, name='view')
]