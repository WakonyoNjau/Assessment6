from EmployeeModule.models import Employee, Registration, NextOfKin
from django import forms

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = 'fullname', 'email', 'emp_code', 'mobile_no', 'position',


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = 'firstname', 'lastname', 'phone_no', 'password',

class NextOfKin(forms.ModelForm):
    class Meta:
        model = NextOfKin
        fields = 'fullname', 'employee_name', 'ID_no', 'phone_no',