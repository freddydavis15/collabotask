from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .models import details

#index page
def index(request):
    return render(request, 'contactus.html')
#to process from html with /add(url) as submit button
@csrf_protect
def fun(request):
    username=request.GET['Name']
    message =request.GET['Message']
    email = request.GET['mailID']
    if username and message and email:
        try:
            a=details()
            a.username=username
            a.message=message
            a.email=email
            a.save()
            body=username + ' \n  ' + message + '\n PLEASE NOTE:- THIS MESSAGE IS A PART OF PROJECT TASK GIVEN BY A PVT. FIRM, AVOID THIS MESSAGE'
            fremail=settings.EMAIL_HOST_USER
            send_mail('CONFIRMATION MAIL',body,fremail,[email])
            messages.info(request,'you will receive a confirmation email')
        except BadHeaderError:
            messages.info(request,'Invalid header found')
        return render(request, 'contactus.html')
    else:
        messages.info(request, 'MAKE SURE YOU ENTERED ALL FIELDS')
        return render(request, 'contactus.html')

#to process as restfull api passing parameters through url
def joke(request, param):
    username=request.GET.get('Name')
    message =request.GET.get('Message')
    email = request.GET.get('mailID')
    if username and message and email:
        try:
            a=details()
            a.username=username
            a.message=message
            a.email=email
            a.save()
            body=username + ' \n  ' + message + '\n PLEASE NOTE:- THIS MESSAGE IS A PART OF PROJECT TASK GIVEN BY A PVT. FIRM, AVOID THIS MESSAGE'
            fremail=settings.EMAIL_HOST_USER
            send_mail('CONFIRMATION MAIL',body,fremail,[email])
            messages.info(request,'you will receive a confirmation email')
        except BadHeaderError:
            messages.info(request,'Invalid header found')
        return render(request, 'contactus.html')
    else:
        messages.info(request, 'MAKE SURE YOU ENTERED ALL FIELDS')
        return render(request, 'contactus.html')

