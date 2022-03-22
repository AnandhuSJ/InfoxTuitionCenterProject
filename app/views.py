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