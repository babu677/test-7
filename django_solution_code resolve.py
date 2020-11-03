#Todo Django

# to create project
'''
django-admin.py startproject company
'''
# to create app
# come back to Project Dir with cd
'''
python3 manage.py startapp staff
'''



#2. ORM

from django.db import models

class Employee_table(models.Model):
    Employee_name = models.CharField('Employee Name', max_length=120)
    Department = models.CharField('Department ', max_length=120)
    Email = models.EmailField(max_length = 254)
    Date_of_birth = models.DateTimeField('Event Date')
    Picture = models.ImageField(upload_to ='imgs/') # # file will be saved to MEDIA_ROOT / imgs

def __str__(self):
        return self.Employee_name




class Department_table(models.Model):
Employee_table=models.Foreignkey(Employee)
    Department_name = models.CharField('Department name', max_length=120)
    Manager = models.CharField('Manager', max_length=120)

def __str__(self):
        return self.Department_name



#3 admin.py

from django.contrib import admin
from .models import Employee, Department
# Register your models here.
List_display=[

………………………..

…………………………………..]

admin.site.register(Employee)
admin.site.register(Department)



# 5
'''
django-admin check auth admin myapp

'''
from django.shortcuts import render

# Create your views here.
import datetime as dt
from django.template.loader import get_template
from django.http.response import HttpResponse

from django.views.generic import ListView
from django.views.generic import DetailView
class PublisherList(ListView):

    model = Employee_table


class PublisherDetail(DetailView):

    model = Employee_table


dt1=dt.datetime.now()

def Department(request):
    t=get_template('')
    c={'':dt1}
    x=t.render(c)
    return HttpResponse(x)




#6.forms.py

forms.py

from django import forms

class Employee_table Form(forms.Form):
    Employee_name=forms.CharField(
        label='Enter Your name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'name here...'
            }
        )
    )
    Department = forms.CharField(
        label='Enter Your department Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder':'father name here...'
            }
        )
    )
    Date_of_birth= forms.datetimefield(
        label='Enter Your date-of-birth',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'enter your mother name'
            }
        )

    )
    picture = forms.image_field(
        label='Enter Your picture',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter your mobile number'
            }
        )

    )
    EmailId = forms.EmailField(
        label='Enter Your EmailId',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter your emailid'
            }
        )

    )


Class department_table Form(form.Forms):

    Department = forms.CharField(
        label='Enter Your department_name,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter your salary here...'
            }
        )

    )
    
