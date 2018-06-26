# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request,'index.html')

def sendemail(request):
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        date=request.POST.get('date')
        email=request.POST.get('email')
        person=request.POST.get('person')
        time=request.POST.get('time')
        
        from_email=email
        to_email=['paragkhuman@gmail.com',]
        subject="Center massage order received"
        contact_message="hello"
        #contact_message=str("Order Details:\n"+"Name:"+name+"Phone No.:"+phone+"Timing Requested:"+time+"Email address:"+email+"NO.of persons:"+person+"Timing:"+timing)

        send_mail(subject,contact_message,from_email,to_email,fail_silently=True)

        return HttpResponseRedirect('/home')
    return HttpResponseRedirect('/home')
    