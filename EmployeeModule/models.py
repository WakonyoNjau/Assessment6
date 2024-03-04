from django.db import models

# create your models here.

class Employee(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    emp_code = models.IntegerField()
    mobile_no = models.CharField(max_length=10)
    position = models.CharField(max_length=10)
    def __str__(self):
        return self.fullname

class Registration(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    def __str__(self):
        return self.firstname

class NextOfKin(models.Model):
    fullname = models.CharField(max_length=50)
    employee_name = models.CharField(max_length=50)
    ID_no = models.IntegerField()
    phone_no = models.CharField(max_length=10)
    def __str__(self):
        return self.fullname
