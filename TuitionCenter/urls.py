"""TuitionCenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include
from django.conf import settings
from django.conf.urls.static import static, serve
from app import views
urlpatterns = [
     re_path('admin/', admin.site.urls),


############################ Admin Section ##################################

    re_path(r'^$', views.Index_Admin, name='Index_Admin'),
    re_path(r'^Registration_Admin$', views.Registration_Admin, name='Registration_Admin'),
    re_path(r'^RegistrationStaff_Admin$', views.RegistrationStaff_Admin, name='RegistrationStaff_Admin'),
    re_path(r'^RegistrationCurrentStaff_Admin$', views.RegistrationCurrentStaff_Admin, name='RegistrationCurrentStaff_Admin'),
    re_path(r'^RegistrationResignedStaff_Admin$', views.RegistrationResignedStaff_Admin, name='RegistrationResignedStaff_Admin'),

    re_path(r'^Staff_Admin$', views.Staff_Admin, name='Staff_Admin'),
    re_path(r'^StaffCurrentstaff_Admin$', views.StaffCurrentstaff_Admin, name='StaffCurrentstaff_Admin'),
    re_path(r'^StaffPreviousstaff_Admin$', views.StaffPreviousstaff_Admin, name='StaffPreviousstaff_Admin'),
    re_path(r'^StaffCurrentstaffProfile_Admin$', views.StaffCurrentstaffProfile_Admin, name='StaffCurrentstaffProfile_Admin'),
    re_path(r'^StaffPreviousstaffProfile_Admin$', views.StaffPreviousstaffProfile_Admin, name='StaffPreviousstaffProfile_Admin'),
    re_path(r'^StaffCurrentstaffAttendance_Admin$', views.StaffCurrentstaffAttendance_Admin, name='StaffCurrentstaffAttendance_Admin'),
    re_path(r'^StaffCurrentstaffAttendanceSort_Admin$', views.StaffCurrentstaffAttendanceSort_Admin, name='StaffCurrentstaffAttendanceSort_Admin'),
    re_path(r'^StaffPreviousstaffAttendance_Admin$', views.StaffPreviousstaffAttendance_Admin, name='StaffPreviousstaffAttendance_Admin'),
    re_path(r'^StaffPreviousstaffAttendanceSort_Admin$', views.StaffPreviousstaffAttendanceSort_Admin, name='StaffPreviousstaffAttendanceSort_Admin'),
    
    re_path(r'^Student_Admin$', views.Student_Admin, name='Student_Admin'),
    re_path(r'^StudentCurrentstudent_Admin$', views.StudentCurrentstudent_Admin, name='StudentCurrentstudent_Admin'),
    re_path(r'^StudentPreviousstudent_Admin$', views.StudentPreviousstudent_Admin, name='StudentPreviousstudent_Admin'),

    re_path(r'^Academic_Admin$', views.Academic_Admin, name='Academic_Admin'),
    re_path(r'^AcademicBatch_Admin$', views.AcademicBatch_Admin, name='AcademicBatch_Admin'),
    re_path(r'^AcademicAddBatch_Admin$', views.AcademicAddBatch_Admin, name='AcademicAddBatch_Admin'),
    re_path(r'^AcademicAddBatchUpdate_Admin$', views.AcademicAddBatchUpdate_Admin, name='AcademicAddBatchUpdate_Admin'),
    re_path(r'^AcademicViewBatch_Admin$', views.AcademicViewBatch_Admin, name='AcademicViewBatch_Admin'),
    
]

