import os
import requests
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import render, redirect
from app.models import *
from datetime import datetime,date
from django.shortcuts import render
from django.conf import settings



# Create your views here.

def Index_Admin(request):
       return render(request, 'Index_Admin.html')

def Registration_Admin(request):
       return render(request, 'Registration_Admin.html')    

def RegistrationStaff_Admin(request):
       return render(request, 'RegistrationStaff_Admin.html')      

def RegistrationCurrentStaff_Admin(request):
       return render(request, 'RegistrationCurrentStaff_Admin.html')     

def RegistrationResignedStaff_Admin(request):
       return render(request, 'RegistrationResignedStaff_Admin.html')                       



def Staff_Admin(request):
       return render(request, 'Staff_Admin.html') 

def StaffCurrentstaff_Admin(request):
       return render(request, 'StaffCurrentstaff_Admin.html') 

def StaffPreviousstaff_Admin(request):
       return render(request, 'StaffPreviousstaff_Admin.html') 

def StaffCurrentstaffProfile_Admin(request):
       return render(request, 'StaffCurrentstaffProfile_Admin.html') 

def StaffPreviousstaffProfile_Admin(request):
       return render(request, 'StaffPreviousstaffProfile_Admin.html') 

def StaffCurrentstaffAttendance_Admin(request):
       return render(request, 'StaffCurrentstaffAttendance_Admin.html')  

def StaffCurrentstaffAttendanceSort_Admin(request):
       return render(request, 'StaffCurrentstaffAttendanceSort_Admin.html')             

def StaffPreviousstaffAttendance_Admin(request):
       return render(request, 'StaffPreviousstaffAttendance_Admin.html') 

def StaffPreviousstaffAttendanceSort_Admin(request):
       return render(request, 'StaffPreviousstaffAttendanceSort_Admin.html')            



def Student_Admin(request):
       return render(request, 'Student_Admin.html') 

def StudentCurrentstudent_Admin(request):
       return render(request, 'StudentCurrentstudent_Admin.html') 

def StudentPreviousstudent_Admin(request):
       return render(request, 'StudentPreviousstudent_Admin.html') 


def Academic_Admin(request):
       return render(request, 'Academic_Admin.html') 

def AcademicBatch_Admin(request):
       return render(request, 'AcademicBatch_Admin.html')

def AcademicAddBatch_Admin(request):
       return render(request, 'AcademicAddBatch_Admin.html') 

def AcademicAddBatchUpdate_Admin(request):
       return render(request, 'AcademicAddBatchUpdate_Admin.html') 


def AcademicViewBatch_Admin(request):
       return render(request, 'AcademicViewBatch_Admin.html') 

       