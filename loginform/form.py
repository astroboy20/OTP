from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from phonenumber_field.formfields import PhoneNumberField

from loginform.models import DataModel

# class CreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username','password']
#     username = forms.Field( widget=forms.TextInput(attrs={
#         "class":"form-control form-control-user", 'placeholder':"Username"}))  
#     password = forms.Field(widget=forms.PasswordInput(attrs={
#          "class":"form-control form-control-user", "id":"password", 'placeholder':"Password"}), label="Password")  
        
#     def save(self, commit=True):
#         instance =super().save(commit=False)
#         instance.username = instance.username
#         if commit:
#             instance.save()
#         return instance


class CreationForm(forms.Form):
    username = forms.Field( widget=forms.TextInput(attrs={
        "class":"form-control form-control-user", 'placeholder':"Username"}))  
    password = forms.Field(widget=forms.PasswordInput(attrs={
         "class":"form-control form-control-user", "id":"password", 'placeholder':"Password"}), label="Password")  
        
    def save(self, commit=True):
        instance =super().save(commit=False)
        instance.username = instance.username
        # if commit:
        #     instance.save()
        return instance

class DataForm(forms.Form):
    fields=['full_name','email','ssn','phone_number']
    full_name = forms.Field( widget=forms.TextInput(attrs={
            "class":"form-control form-control-user", 'placeholder':"Username"}),label='Full Name') 
    email = forms.Field(widget=forms.EmailInput(attrs={
            "class":"form-control form-control-user", 'placeholder':"Email"}),label='Email')
    ssn = forms.Field(widget=forms.NumberInput(attrs={
            "class":"form-control form-control-user", 'placeholder':"Social Security Number"}),label='Social Security Number')
    phone_number = PhoneNumberField(widget=forms.NumberInput(attrs={
            "class":"form-control form-control-user", 'placeholder':"Phone Number"}),label='Phone Number')
            
    def save(self, commit=True):
        instance =super(DataForm,self).save(commit=False)
        instance.full_name = instance.email
        if commit:
            instance.save()
        return instance