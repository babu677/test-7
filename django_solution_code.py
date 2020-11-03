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
    Department_table =models.CharField('Department table', max_length=120)
    Department_name = models.CharField('Department name', max_length=120)
    Manager = models.CharField('Manager', max_length=120)


# 5
'''
django-admin check auth admin myapp
'''

from django.views.generic import ListView
from django.views.generic import DetailView
class PublisherList(ListView):

    model = Employee_table


class PublisherDetail(DetailView):

    model = Employee_table
