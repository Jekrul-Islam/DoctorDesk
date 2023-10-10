
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import appointment,patient,contact
from .form import *
from django.http import HttpResponse


# Create your views here.
def home(request):
    #return HttpResponse("<h1>This is my homepage</h1>")
    return render(request,'home.html')

class SignupView(View):
    def get(self,request):
        fm = SignUpForm()
        return render(request,"signup.html",{'form':fm})

    def post(self, request):
        fm= SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Sign up Success !")
            return redirect("/signup")
        else:
            return render(request,"signup.html",{'form':fm})

class LoginView(View):
    def get(self, request):
        fm = LoginForm()
        
        return render(request, 'login.html', {'form': fm})

    def post(self, request):
        fm = LoginForm(request, data=request.POST)

        print(fm.is_valid())
        if fm.is_valid():

            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            print(user)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:

                messages.success(request, 'Profile details updated.')
                return render(request, 'login.html', {'from': fm})


        else:
            fm = LoginForm()
            messages.error(request, 'Invalid Login Details.')
            return render(request, 'login.html', {'form': fm})

def About(request):

    return render(request,"about.html")

def Contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        gender=request.POST['gender']
        comments=request.POST['comments']
        obj=contact(name=name,email=email,phone=phone,gender=gender,comments=comments)
        obj.save()
    msg=contact.objects.all()
    obj={
        "contacts":msg
    }

        
    
    return render(request,'contact.html',obj)

def Appointment(request):
    if request.method=='POST':
        username=request.user
        name=request.POST['name']

        contact=request.POST['contact']
        date=request.POST['date']
        time=request.POST['time']
        doctor=request.POST['semester']
        symtoms=request.POST['symtoms']

        
        obj=appointment(username=username,doctor=doctor,name=name,phone=contact,date=date,time=time,symtoms=symtoms)
        obj.save()
    
    appointments=appointment.objects.filter(username=request.user)
    data={
        "appointments":appointments
    }


    appointments_list = appointment.objects.all()

    data.update({'list_patient':appointments_list})

    return render(request,'appointment.html',data)


def delete(request, id):
    list = appointment.objects.get(id=id)
    list.delete()
    return redirect('appointment')

def profile(request):
    context = {
        'user': request.user
    }
    return render(request,'profile.html',context)

