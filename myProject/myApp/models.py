from django.db import models

# Create your models here.
# models.Model gives behaviour to model
class EmployeeData(models.Model):
    emp_name=models.CharField(max_length=20)
    emp_pwd=models.CharField(max_length=20)
    emp_email=models.EmailField(max_length=20)
    emp_mob=models.BigIntegerField()
    emp_dept=models.CharField(max_length=8)
    emp_dob=models.DateField()
    emp_img=models.ImageField(upload_to='uploadedFiles',null=True)

class Booking(models.Model):
    r_type=models.CharField(max_length=10)
    r_no=models.IntegerField()
    r_dfrom=models.DateField()
    r_dto=models.DateField()
    r_payment=models.CharField(max_length=15)
    r_unm=models.CharField(max_length=15,null=True)
   
class UserData(models.Model):
    user_name=models.CharField(max_length=20)
    user_mob=models.BigIntegerField()
    user_email=models.EmailField(max_length=20)
    user_pwd=models.CharField(max_length=20)