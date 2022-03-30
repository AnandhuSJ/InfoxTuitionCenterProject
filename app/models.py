from django.contrib.auth.models import User
from django.db import models

# Create your models here.






class batch(models.Model):
    batch_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
            return self.batch_name


class class_registration(models.Model):
    batch_name = models.ForeignKey(batch,on_delete=models.DO_NOTHING,related_name='batchclass',null=True,blank=True)
    class_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    
    def __str__(self):
            return self.class_name
class designation(models.Model):
    batch_name= models.ForeignKey(batch, on_delete=models.DO_NOTHING , related_name='batchdesignation',null=True,blank=True)
    designation = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    files=models.FileField(upload_to = 'images/', null=True, blank=True)

    def __str__(self):
        return self.designation

class user_registration(models.Model):
    designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING,
                                    related_name='userdesignation', null=True, blank=True)
    batch= models.ForeignKey(batch, on_delete=models.DO_NOTHING,
                                    related_name='userbatch', null=True, blank=True)
    class_registration= models.ForeignKey(class_registration, on_delete=models.DO_NOTHING,
                                    related_name='class_registration', null=True, blank=True)
    email = models.EmailField(max_length=240, null=True)      
    fullname = models.CharField(max_length=240, null=True)                          
    
    dateofbirth = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
   
    mobile = models.CharField(max_length=240, null=True)
   
    employee_id = models.CharField(max_length=240,null=True,default='') 	
    student_id = models.CharField(max_length=240,null=True,default='')
    password = models.CharField(max_length=240, null=True)
    
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    attitude = models.IntegerField(default='0')
    creativity = models.IntegerField(default='0')
    workperformance = models.IntegerField(default='0')
    joiningdate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)

    dateofappointment = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    
    status = models.CharField(max_length=240, null=True, default='')
   
    
 
    def __str__(self):
        return self.fullname


class attendance(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING,
                             related_name='attendanceuser', null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    
    status = models.CharField(max_length=200)
    
    def __str__(self):
        return self.user

class payment_details(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING,related_name='paymentuser', null=True, blank=True)    
    account_no = models.CharField(max_length=200, null=True, default='')
    ifsc =  models.CharField(max_length=200, null=True, default='')
    bank_name = models.CharField(max_length=240, null=True, default='')
    bank_branch = models.CharField(max_length=240, null=True, default='')
    payment_date = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    payment_amount = models.IntegerField(default='0')
    payment_status = models.CharField(max_length=200, null=True, default='')

    def __str__(self):
        return self.user