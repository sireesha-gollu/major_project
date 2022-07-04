from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import smtplib
import io
#from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from . import models
import smtplib
from django.core.mail import send_mail

from . import ecelgamal 





config = {
        "apiKey" : "9Va7NU7FhlX6krcgVVZj41z3wT1k5qJnY7TYXZFI",
        "authDomain" : "majorproject-node1234.firebaseapp.com",
        "databaseURL" : "https://majorproject-node1234-default-rtdb.firebaseio.com/",
        "storageBucket" : "majorproject-node1234.appspot.com"
}



private_key="62284108405421925867042857897045013910476207735332576701727340378561582474450"
# Create your views here.
def data_fetchedByCloud():
    encrypted_ciphers={
    "cipher1": {
      "X": "2624152952072237030387803539892739855697462819691793666860200218304960881898",
      "Y": "62394012599864944934874506552273073146061173590601816423666632557841125446437"
    },
    "cipher2": {
      "X": "27409902633099241621785471258611746029691045314578490210115670056060205894414",
      "Y": "99997017779405687575526084489353182949249021181435686353025901384068825698773"
    },
    "private key": "62284108405421925867042857897045013910476207735332576701727340378561582474450"
    }
    priv_key=int(encrypted_ciphers["private key"])
    C1_x=int(encrypted_ciphers["cipher1"]["X"])
    C1_y=int(encrypted_ciphers["cipher1"]["Y"])
    C2_x=int(encrypted_ciphers["cipher2"]["X"])
    C2_y=int(encrypted_ciphers["cipher2"]["Y"])
    C1=ecelgamal.Point(C1_x,C1_y,ecelgamal.secp256k1)
    C2=ecelgamal.Point(C2_x,C2_y,ecelgamal.secp256k1)
    decrypted_data=ecelgamal.decryption(priv_key,C1,C2)
    return priv_key,decrypted_data

def button(request):
    return render(request, 'view_report')
def home(request):
    return render(request,'home.html')
def adminpage(request):
    return render(request,'adminpage.html')
def about(request):
    return render(request,'about.html')

def send_email(request):
    if request.method=="POST":
        email=request.POST['email']
        msg="Use This Key for Download File"
        subject="Key Request Activation Response"
        message = '\n{} \nPrivate Key : {}'.format(msg,private_key)
        recipient_list = [email,]
        email_from = settings.DEFAULT_FROM_EMAIL
        send_mail( subject, message, email_from, recipient_list )
        data="Email Sent Successfully!!!"
        data=data
        return render(request,'view_report.html',{'data':data})
    return render(request,'view_report.html')
    #return render(request,'view_report.html')

def view_data(request):
    return render(request,"view_data.html")
def view(request):
    return render(request,"view.html")   
def contactus(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        subject = f'Message from {name}'
        message = f'''Email:  {email} 
        {message}'''
        email_from = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['18jg1a0529.sireesha@gvpcew.ac.in', ]
        send_mail( subject, message, email_from, recipient_list )
        messages.info(request,'Message sent!!!')
        return render(request,'contactus.html')
    return render(request,'contactus.html')
def userpage(request):
    return render(request,'userpage.html')
def adminlogin(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('adminpage')
        else:
            messages.info(request,'Incorrect Username or Password!!!')
            return redirect('adminlogin')
    else:
        return render(request,'adminlogin.html')


def key(request):
    if request.method =='POST':
        password=request.POST['password']
        if password==private_key:
            return redirect('view')  
        else:
            messages.info(request,'Incorrect Key Entered!!!')
            return redirect('key')
    else:
        return render(request,'key.html')

def view_report(request):
    return render(request,'view_report.html')

def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('userpage')
        else:
            messages.info(request,'Incorrect Username or Password!!!')
            return redirect('login')
    else:
        return render(request,'login.html')

def registration(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username is already taken!!!')
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email is already Exists!!!')
                return redirect('registration')
            else:
                user=User.objects.create_user(username=username,password= password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
        else:
            messages.info(request,'Password not matching!!!')
        return redirect('login')
    else:
        return render(request,'registration.html')
