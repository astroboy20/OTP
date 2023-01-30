from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class DataModel(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    ssn = models.IntegerField(max_length=20)
    phone_number = PhoneNumberField()

    def  __str__(self) :
        return self.full_name