from django.contrib.auth import logout
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


class RegisterPatientView:
    pass


urlpatterns = [
    path('', home,name="home"),
    path('home', home,name="home"),
    path('signup',SignupView.as_view(),name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page ='login'), name ='logout'),
    path('about',About,name='about'),
    path('contact',Contact,name='contact'),
    path('appointment',Appointment,name='appointment'),
    path('delete/<int:id>',delete, name='delete'),
    path('profile', profile, name='profile'),

]
