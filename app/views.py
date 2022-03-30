import os
import requests
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import render, redirect
from app.models import *
from datetime import datetime,date
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth
from django.contrib.auth.hashers import check_password, make_password


#Create your views here.

def login(request):
    
    
    Man = designation.objects.get(designation='manager')
    

    if request.method == 'POST':
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=Man.id).exists():
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['Man_id'] = member.id
            request.session['Man_id'] = member.designation_id
           
            if request.session.has_key('Man_id'):
                Man_id = request.session['Man_id']
            else:
                variable = "dummy"
            mem = user_registration.objects.filter(id=Man_id)
            return render(request, 'MAN_index.html', {'mem':mem})

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.get(email=email)
        if user is not None:
            pwd_valid = check_password(password, user.password)
            if pwd_valid:
                request.session['SAdm_id'] = user.id
                return redirect('Index_Admin')
            else:
            
             return render(request ,'Login.html')
    return render(request,'Login.html')

def Index_Admin(request):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
        
       return render(request, 'Index_Admin.html',{'mem':mem})

def Registration_Admin(request):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       Desig = designation.objects.all()
       Student = designation.objects.filter(designation = 'Student')
       Staff = designation.objects.filter(designation = 'Staff')
       return render(request, 'Registration_Admin.html',{'mem':mem,'Desig':Desig,'Student':Student,'Staff':Staff})    

def RegistrationStaff_Admin(request,id):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       id=id
       return render(request, 'RegistrationStaff_Admin.html',{'mem':mem})      

def RegistrationStudent_Admin(request,id):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id) 
       id=id    
       return render(request, 'RegistrationStudent_Admin.html',{'mem':mem})       

def RegistrationCurrentStaff_Admin(request):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       des = designation.objects.get(designation='staff')
       CStaff = user_registration.objects.filter(designation_id = des).filter(status='active' or 'Active').all().order_by('-id')
       batc = batch.objects.all()
       class_reg = class_registration.objects.all()
       payment = payment_details.objects.all().filter
       return render(request, 'RegistrationCurrentStaff_Admin.html',{'mem':mem,'des':des,'CStaff':CStaff,'batc':batc,'class_reg':class_reg,'payment':payment})  

def RegistrationCurrentStaff_Adminsave(request,id):
    
   
    if request.method == 'POST':
       a = user_registration.objects.get(id=id)
   
       a.status = request.POST['status']
       BatchId = request.POST['batch'] 
       a.batch_id = BatchId 
       ClassId = request.POST['class'] 
       a.class_registration_id = ClassId
       a.save()
     
       return redirect('RegistrationCurrentStaff_Admin')




def RegistrationCurrentStaffAdmin_update(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/') 
        SAdm = user_registration.objects.filter(id=SAdm_id)
        
        mem1 = user_registration.objects.get(id=id)
        pay = payment_details.objects.filter(user_id=id)
        bac = batch.objects.all()
        clss = class_registration.objects.all()
        
        return render(request,'RegistrationCurrentStaffAdmin_update.html',{'pay':pay,'mem1':mem1,'clss':clss,'bac':bac,'SAdm':SAdm})
    else:
        return redirect('/')




def RegistrationCurrentStaffAdmin_updatessave(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/') 
        SAdm = user_registration.objects.filter(id=SAdm_id) 
    a = user_registration.objects.get(id=id)
    b = payment_details.objects.get(user_id=id)
    if request.method == 'POST':
       a.fullname = request.POST['name']
       a.email = request.POST['email']
       a.contactnumber = request.POST['mobile']
       a.status = request.POST['status']
       a.dateofappointment  =  request.POST['dateofappo']
       a.employeeid =  request.POST['employeeid'] 
       BatchId = request.POST['batch'] 
       a.batch_id = BatchId 
       ClassId = request.POST['class'] 
       a.class_registration_id = ClassId
       a.save()
              
       b.payment_amount = request.POST['payment']
       b.save()       

    return render(request,'RegistrationCurrentStaff_Admin.html')


def RegistrationCurrentStaffAdmin_delete(request,id):
    
    m =   user_registration.objects.get(id = id)
    m.delete()
    return redirect('RegistrationCurrentStaff_Admin')

def RegistrationResignedStaff_Admin(request):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       des1 = designation.objects.get(designation='staff')
       RStaff = user_registration.objects.filter(designation_id = des1).filter(status='resigned' or 'Resigned').all().order_by('-id')
       batc1 = batch.objects.all()
       class_reg1 = class_registration.objects.all()
       payment1 = payment_details.objects.all()
       return render(request, 'RegistrationResignedStaff_Admin.html',{'mem':mem,'des1':des1,'RStaff':RStaff,'batc1':batc1,'class_reg1':class_reg1,'payment1':payment1})  


def RegistrationResignedStaffAdmin_update(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/') 
        SAdm = user_registration.objects.filter(id=SAdm_id)
        
        mem1 = user_registration.objects.get(id=id)
        pay = payment_details.objects.filter(user_id=id)
        bac = batch.objects.all()
        clss = class_registration.objects.all()
        
        return render(request,'RegistrationResignedStaffAdmin_update.html',{'pay':pay,'mem1':mem1,'clss':clss,'bac':bac,'SAdm':SAdm})
    else:
        return redirect('/')




def RegistrationResignedStaffAdmin_updatessave(request,id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/') 
        SAdm = user_registration.objects.filter(id=SAdm_id)    
    a = user_registration.objects.get(id=id)
    b = payment_details.objects.get(user_id=id)
    if request.method == 'POST':
       a.fullname = request.POST['name']
       a.email = request.POST['email']
       a.contactnumber = request.POST['mobile']
       a.status = request.POST['status'] 
       BatchId = request.POST['batch'] 
       a.batch_id = BatchId 
       ClassId = request.POST['class'] 
       a.class_registration_id = ClassId
       a.save()
              
       b.payment_amount = request.POST['payment']
       b.save()   

    return redirect('RegistrationResignedStaff_Admin')


def RegistrationResignedStaffAdmin_delete(request,id):
    
    
    m =   user_registration.objects.get(id = id)
    m.delete()
    return redirect('RegistrationResignedStaff_Admin')


def RegistrationCurrentStudent_Admin(request):
        if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=SAdm_id)
        des = designation.objects.get(designation='student')
        CStudent = user_registration.objects.filter(designation_id = des).filter(status='active' or 'Active').all().order_by('-id')
        batc2 = batch.objects.all()
        class_reg2 = class_registration.objects.all()
        return render(request, 'RegistrationCurrentStudent_Admin.html',{'mem':mem,'des':des,'CStudent':CStudent,'batc2':batc2,'class_reg2':class_reg2})     

def RegistrationCurrentStudent_Adminsave(request,id):
    
   
    if request.method == 'POST':
       a = user_registration.objects.get(id=id)
   
       BatchId = request.POST['batch'] 
       a.batch_id = BatchId 
       ClassId = request.POST['class'] 
       a.class_registration_id = ClassId
       a.save()
     
       return redirect('RegistrationCurrentStudent_Admin')


def RegistrationPreviousstudent_Admin(request):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       des = designation.objects.get(designation='student')
       PStudent = user_registration.objects.filter(designation_id = des).filter(status='graduated' or 'Graduated').all().order_by('-id')
       batc3 = batch.objects.all()
       class_reg3 = class_registration.objects.all()
       return render(request, 'RegistrationPreviousstudent_Admin.html',{'mem':mem,'des':des,'PStudent':PStudent,'batc3':batc3,'class_reg3':class_reg3})                              



def Staff_Admin(request):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       return render(request, 'Staff_Admin.html',{'mem':mem}) 

def StaffCurrentstaff_Admin(request):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       des = designation.objects.get(designation='staff')
       SCurrentstaff = user_registration.objects.filter(designation_id = des).filter(status='active' or 'Active').all().order_by('-id')
       return render(request, 'StaffCurrentstaff_Admin.html',{'mem':mem,'des':des,'SCurrentstaff':SCurrentstaff}) 

def StaffPreviousstaff_Admin(request):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       des = designation.objects.get(designation='staff')
       PCurrentstaff = user_registration.objects.filter(designation_id = des).filter(status='resigned' or 'Resgined').all().order_by('-id')
       return render(request, 'StaffPreviousstaff_Admin.html',{'mem':mem,'des':des,'PCurrentstaff':PCurrentstaff}) 

def StaffCurrentstaffProfile_Admin(request,id):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       CStaffProfile = user_registration.objects.get(id = id)
       return render(request, 'StaffCurrentstaffProfile_Admin.html',{'mem':mem,'CStaffProfile':CStaffProfile}) 

def StaffPreviousstaffProfile_Admin(request,id):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       
       PStaffProfile = user_registration.objects.get(id = id)
       return render(request, 'StaffPreviousstaffProfile_Admin.html',{'mem':mem,'PStaffProfile':PStaffProfile}) 

def StaffCurrentstaffAttendance_Admin(request,id):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       id = id
       return render(request, 'StaffCurrentstaffAttendance_Admin.html',{'mem':mem,'id':id})  

def StaffCurrentstaffAttendanceSort_Admin(request,id):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       id=id
       if request.method == "POST":
            fromdate = request.POST.get('from')
            todate = request.POST.get('to') 
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id = id)
       return render(request,'StaffCurrentstaffAttendanceSort_Admin.html',{'mem':mem,'mem1':mem1,'id':id})            

def StaffPreviousstaffAttendance_Admin(request,id):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       id = id
       return render(request, 'StaffPreviousstaffAttendance_Admin.html',{'mem':mem,'id':id})  

def StaffPreviousstaffAttendanceSort_Admin(request,id):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       id=id
       if request.method == "POST":
            fromdate = request.POST.get('from')
            todate = request.POST.get('to') 
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id = id)
       return render(request,'StaffPreviousstaffAttendanceSort_Admin.html',{'mem':mem,'mem1':mem1,'id':id})


def Student_Admin(request):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       return render(request, 'Student_Admin.html',{'mem':mem}) 

def StudentCurrentstudent_Admin(request):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       des = designation.objects.get(designation='student')
       SCurrentstudent = user_registration.objects.filter(designation_id = des).filter(status='active' or 'Active')
       return render(request, 'StudentCurrentstudent_Admin.html',{'mem':mem,'des':des,'SCurrentstudent':SCurrentstudent}) 

def StudentPreviousstudent_Admin(request):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       des = designation.objects.get(designation='student')
       PCurrentstudent = user_registration.objects.filter(designation_id = des).filter(status='graduated' or 'Graduated')
       return render(request, 'StudentPreviousstudent_Admin.html',{'mem':mem,'des':des,'PCurrentstudent':PCurrentstudent}) 

def StudentCurrentstudentProfile_Admin(request,id):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       CStudentProfile = user_registration.objects.get(id = id)
       return render(request, 'StudentCurrentstudentProfile_Admin.html',{'mem':mem,'CStudentProfile':CStudentProfile})

def StudentPreviousstudentProfile_Admin(request,id):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       PStudentProfile = user_registration.objects.get(id = id)
       return render(request, 'StudentPreviousstudentProfile_Admin.html',{'mem':mem,'PStudentProfile':PStudentProfile})

def StudentCurrentstudentAttendance_Admin(request,id):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       id = id
       return render(request, 'StudentCurrentstudentAttendance_Admin.html',{'mem':mem,'id':id}) 

def StudentCurrentstudentAttendanceSort_Admin(request,id):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       id=id
       if request.method == "POST":
            fromdate = request.POST.get('from')
            todate = request.POST.get('to') 
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id = id)
       return render(request,'StudentCurrentstudentAttendanceSort_Admin.html',{'mem':mem,'mem1':mem1,'id':id})

def StudentPreviousstudentAttendance_Admin(request,id):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       id = id
       return render(request, 'StudentPreviousstudentAttendance_Admin.html',{'mem':mem,'id':id})
      
def StudentPreviousstudentAttendanceSort_Admin(request,id):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       id=id
       if request.method == "POST":
            fromdate = request.POST.get('from')
            todate = request.POST.get('to') 
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id = id)
       return render(request,'StudentPreviousstudentAttendanceSort_Admin.html',{'mem':mem,'mem1':mem1,'id':id})        



def Academic_Admin(request):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       return render(request, 'Academic_Admin.html',{'mem':mem}) 

def AcademicBatch_Admin(request):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       return render(request, 'AcademicBatch_Admin.html',{'mem':mem})

def AcademicAddBatch_Admin(request):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       Batc = batch.objects.all()
       return render(request, 'AcademicAddBatch_Admin.html',{'mem':mem,'Batc':Batc,}) 


def AcademicAddBatch_Adminsave(request):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       if request.method == 'POST':
              desc = request.POST['discrip']
       ba = request.POST['batch']
       a=batch(description=desc,batch_name=ba)
       a.save()
       m="Batch added Successfully"
       return render(request, 'AcademicAddBatch_Admin.html',{'m':m,'mem':mem}) 

def AcademicAddBatchUpdate_Admin(request,id):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       var= batch.objects.filter(id=id)
       var1= batch.objects.get(id=id)
       batc = batch.objects.all()
       return render(request, 'AcademicAddBatchUpdate_Admin.html',{'mem':mem,'batc':batc,'var':var,'var1':var1}) 

def AcademicAddBatchUpdate_Adminsave(request,id):
       if 'SAdm_id' in request.session:
              if request.session.has_key('SAdm_id'):
                     SAdm_id = request.session['SAdm_id']
              else:
                     return redirect('/')
              mem = user_registration.objects.filter(id=SAdm_id)
              if request.method == 'POST':
                     a=batch.objects.get(id=id)
                     a.desc = request.POST.get('discrip')
                     a.batch_name = request.POST.get('batch')
                     a.save()
                     m="Batch updated Successfully"
              return render(request,'AcademicAddBatch_Admin.html',{'m':m,'mem':mem})


def AcademicViewBatch_Admin(request):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)

       batc = batch.objects.all()
       clss = class_registration.objects.all()
       return render(request, 'AcademicViewBatch_Admin.html',{'mem':mem,'batc':batc,'clss':clss})

def AcademicAddBatch_Admindelete(request,id):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       m =batch.objects.get(id = id)
       n =class_registration.objects.get(batch_name_id=id)
       m.delete()
       n.delete()
       return render(request,'AcademicViewBatch_Admin.html',{'mem':mem})        

       

def MAN_Index(request):
       if request.session.has_key('Man_id'):
            Man_id = request.session['Man_id']
       else:
            return redirect('/')      
       man = user_registration.objects.filter(id=Man_id)
       return render(request, 'MAN_Index.html',{'man':man}) 

def MAN_Academic(request):
       if request.session.has_key('Man_id'):
            Man_id = request.session['Man_id']
       else:
            return redirect('/')     
       man = user_registration.objects.filter(id=Man_id)
       
       return render(request, 'MAN_Academic.html',{'man':man}) 

def MAN_AcademicClass(request):
       if request.session.has_key('Man_id'):
            Man_id = request.session['Man_id']
       else:
            return redirect('/')     
       man = user_registration.objects.filter(id=Man_id)
       return render(request, 'MAN_AcademicClass.html',{'man':man}) 

def MAN_AcademicAddClass(request):
       if request.session.has_key('Man_id'):
           Man_id = request.session['Man_id']
       else:
            return redirect('/')    
       man = user_registration.objects.filter(id=Man_id)
       Batc = batch.objects.all()
       return render(request, 'MAN_AcademicAddClass.html',{'man':man,'Batc':Batc})        


def MAN_AcademicAddClasssave(request):
    if request.session.has_key('Man_id'):
        Man_id = request.session['Man_id']
    else:
            return redirect('/')
    man = user_registration.objects.filter(id=Man_id)        
    if request.method == 'POST':
       newclass = request.POST['class']
       desc = request.POST['discrip']
       ba = request.POST['batch']
       a=class_registration(class_name=newclass,description=desc,batch_name_id=ba)
       a.save()
       m="Class added Successfully"
    return render(request,'MAN_AcademicAddClass.html',{'m':m,'man':man})                     