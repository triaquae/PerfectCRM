from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from crm import forms
from crm import models
from crm import admin
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

@login_required
def my_courses(request):
    '''每个学员的课程列表'''
    return render(request,"crm/my_courses.html")

@login_required
def my_grade(request):
    return render(request,'stu/my_grade.html')