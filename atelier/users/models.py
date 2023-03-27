from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator , MinLengthValidator
from django.core.exceptions import ValidationError
# Create your models here.

def cin_valid(val):
    if len(val) != 8 : 
        raise ValidationError("la longueur de cin doit etre egale a 8")
    return val    

def email_valid(v):
    if str(v).endswith('esprit.tn') == False:
        raise ValidationError('Votre email est invalide et doit se terminer par @esprit.tn')
    return v


class Person(AbstractUser):
    cin = models.CharField(primary_key=True, max_length=8)
    email =models.EmailField(unique=True)
    username=models.CharField(unique=True, max_length=8)
    USERNAME_FIELD ='username'