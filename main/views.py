from .forms import ResponseForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from email.message import EmailMessage
from django.contrib import messages
import ssl
import os
from django.core.mail import BadHeaderError, send_mail
from boto.s3.connection import S3Connection
from decouple import config


def home(request):
    return render(request, "main/home.html", {})

def resume(request):
    return render(request, "main/resume.html", {})

def projects(request):
    return render(request, "main/projects.html", {})

def contact(request):
    form = ResponseForm()

    if "responded" not in request.session:
        request.session["responded"] = False
        request.session["name"] = None

    if request.method == "POST" and request.session["responded"] == False:
        form = ResponseForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            email = form.cleaned_data['email']
            response = form.cleaned_data['response']

            if fname and lname and email and response:
                try:
                    send_mail(
                        "Website User Message: "+fname+" "+lname+lname,
                        "Name: "+fname+" "+lname+", Email: "+email+", Message: "+response,
                        email,
                        [str(os.environ.get('EMAIL_USER')),],
                        fail_silently=False,
                    )
                    request.session["responded"] = True
                    request.session["name"] = fname
                    redirect('main:contact')
                    
                # protect against header injection
                except BadHeaderError:
                    messages.error(request, ("An error has occured! Please try again!"))
                    return redirect('main:contact')
          
    return render(request, "main/contact.html", {
        "form": form,
        "responded": request.session["responded"],
        "name": request.session["name"],
    })
