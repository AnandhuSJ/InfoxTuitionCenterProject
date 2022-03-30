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
    re_path(r'^$', views.login, name='login'),
    re_path(r'^Index_Admin$', views.Index_Admin, name='Index_Admin'),  
    re_path(r'^Registration_Admin$', views.Registration_Admin, name='Registration_Admin'),
    re_path(r'^RegistrationStaff_Admin/(?P<id>\d+)/$', views.RegistrationStaff_Admin, name='RegistrationStaff_Admin'),
    re_path(r'^RegistrationStudent_Admin/(?P<id>\d+)/$', views.RegistrationStudent_Admin, name='RegistrationStudent_Admin'),
    re_path(r'^RegistrationCurrentStaff_Admin$', views.RegistrationCurrentStaff_Admin, name='RegistrationCurrentStaff_Admin'),
    re_path(r'^RegistrationCurrentStaff_Adminsave/(?P<id>\d+)/$', views.RegistrationCurrentStaff_Adminsave, name='RegistrationCurrentStaff_Adminsave'),
    re_path(r'^RegistrationCurrentStaffAdmin_update/(?P<id>\d+)/$', views.RegistrationCurrentStaffAdmin_update, name='RegistrationCurrentStaffAdmin_update'),
    re_path(r'^RegistrationCurrentStaffAdmin_updatessave/(?P<id>\d+)/$', views.RegistrationCurrentStaffAdmin_updatessave, name='RegistrationCurrentStaffAdmin_updatessave'),
    re_path(r'^RegistrationCurrentStaffAdmin_delete/(?P<id>\d+)/$', views.RegistrationCurrentStaffAdmin_delete, name='RegistrationCurrentStaffAdmin_delete'),
    re_path(r'^RegistrationResignedStaffAdmin_update/(?P<id>\d+)/$', views.RegistrationResignedStaffAdmin_update, name='RegistrationResignedStaffAdmin_update'),
    re_path(r'^RegistrationResignedStaffAdmin_updatessave/(?P<id>\d+)/$', views.RegistrationResignedStaffAdmin_updatessave, name='RegistrationResignedStaffAdmin_updatessave'),
    re_path(r'^RegistrationResignedStaffAdmin_delete$', views.RegistrationResignedStaffAdmin_delete, name='RegistrationResignedStaffAdmin_delete'),
    re_path(r'^RegistrationResignedStaff_Admin$', views.RegistrationResignedStaff_Admin, name='RegistrationResignedStaff_Admin'),
    re_path(r'^RegistrationCurrentStudent_Admin$', views.RegistrationCurrentStudent_Admin, name='RegistrationCurrentStudent_Admin'),
    re_path(r'^RegistrationCurrentStudent_Adminsave/(?P<id>\d+)/$', views.RegistrationCurrentStudent_Adminsave, name='RegistrationCurrentStudent_Adminsave'),
    re_path(r'^RegistrationPreviousstudent_Admin$', views.RegistrationPreviousstudent_Admin, name='RegistrationPreviousstudent_Admin'),

    re_path(r'^Staff_Admin$', views.Staff_Admin, name='Staff_Admin'),
    re_path(r'^StaffCurrentstaff_Admin$', views.StaffCurrentstaff_Admin, name='StaffCurrentstaff_Admin'),
    re_path(r'^StaffPreviousstaff_Admin$', views.StaffPreviousstaff_Admin, name='StaffPreviousstaff_Admin'),
    re_path(r'^StaffCurrentstaffProfile_Admin/(?P<id>\d+)/$', views.StaffCurrentstaffProfile_Admin, name='StaffCurrentstaffProfile_Admin'),
    re_path(r'^StaffPreviousstaffProfile_Admin/(?P<id>\d+)/$', views.StaffPreviousstaffProfile_Admin, name='StaffPreviousstaffProfile_Admin'),
    re_path(r'^StaffCurrentstaffAttendance_Admin/(?P<id>\d+)/$', views.StaffCurrentstaffAttendance_Admin, name='StaffCurrentstaffAttendance_Admin'),
    re_path(r'^StaffCurrentstaffAttendanceSort_Admin/(?P<id>\d+)/$', views.StaffCurrentstaffAttendanceSort_Admin, name='StaffCurrentstaffAttendanceSort_Admin'),
    re_path(r'^StaffPreviousstaffAttendance_Admin/(?P<id>\d+)/$', views.StaffPreviousstaffAttendance_Admin, name='StaffPreviousstaffAttendance_Admin'),
    re_path(r'^StaffPreviousstaffAttendanceSort_Admin/(?P<id>\d+)/$', views.StaffPreviousstaffAttendanceSort_Admin, name='StaffPreviousstaffAttendanceSort_Admin'),
    
    re_path(r'^Student_Admin$', views.Student_Admin, name='Student_Admin'),
    re_path(r'^StudentCurrentstudent_Admin$', views.StudentCurrentstudent_Admin, name='StudentCurrentstudent_Admin'),
    re_path(r'^StudentPreviousstudent_Admin$', views.StudentPreviousstudent_Admin, name='StudentPreviousstudent_Admin'),
    re_path(r'^StudentCurrentstudentProfile_Admin/(?P<id>\d+)/$', views.StudentCurrentstudentProfile_Admin, name='StudentCurrentstudentProfile_Admin'),
    re_path(r'^StudentPreviousstudentProfile_Admin/(?P<id>\d+)/$', views.StudentPreviousstudentProfile_Admin, name='StudentPreviousstudentProfile_Admin'),
    re_path(r'^StudentCurrentstudentAttendance_Admin/(?P<id>\d+)/$', views.StudentCurrentstudentAttendance_Admin, name='StudentCurrentstudentAttendance_Admin'),
    re_path(r'^StudentCurrentstudentAttendanceSort_Admin/(?P<id>\d+)/$', views.StudentCurrentstudentAttendanceSort_Admin, name='StudentCurrentstudentAttendanceSort_Admin'),
    re_path(r'^StudentPreviousstudentAttendance_Admin/(?P<id>\d+)/$', views.StudentPreviousstudentAttendance_Admin, name='StudentPreviousstudentAttendance_Admin'),
    re_path(r'^StudentPreviousstudentAttendanceSort_Admin/(?P<id>\d+)/$', views.StudentPreviousstudentAttendanceSort_Admin, name='StudentPreviousstudentAttendanceSort_Admin'),

    re_path(r'^Academic_Admin$', views.Academic_Admin, name='Academic_Admin'),
    re_path(r'^AcademicBatch_Admin$', views.AcademicBatch_Admin, name='AcademicBatch_Admin'),
    re_path(r'^AcademicAddBatch_Admin$', views.AcademicAddBatch_Admin, name='AcademicAddBatch_Admin'),
    re_path(r'^AcademicAddBatch_Adminsave$', views.AcademicAddBatch_Adminsave, name='AcademicAddBatch_Adminsave'),
    re_path(r'^AcademicAddBatchUpdate_Admin/(?P<id>\d+)/$', views.AcademicAddBatchUpdate_Admin, name='AcademicAddBatchUpdate_Admin'),
    re_path(r'^AcademicAddBatchUpdate_Adminsave/(?P<id>\d+)/$', views.AcademicAddBatchUpdate_Adminsave, name='AcademicAddBatchUpdate_Adminsave'),
    re_path(r'^AcademicViewBatch_Admin$', views.AcademicViewBatch_Admin, name='AcademicViewBatch_Admin'),
    re_path(r'^AcademicAddBatch_Admindelete/(?P<id>\d+)/$', views.AcademicAddBatch_Admindelete, name='AcademicAddBatch_Admindelete'),


     re_path(r'^MAN_Index$', views.MAN_Index, name='MAN_Index'),
     re_path(r'^MAN_Academic$', views.MAN_Academic, name='MAN_Academic'),
     re_path(r'^MAN_AcademicClass$', views.MAN_AcademicClass, name='MAN_AcademicClass'),
     re_path(r'^MAN_AcademicAddClass$', views.MAN_AcademicAddClass, name='MAN_AcademicAddClass'),
     re_path(r'^MAN_AcademicAddClasssave$', views.MAN_AcademicAddClasssave, name='MAN_AcademicAddClasssave'),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
