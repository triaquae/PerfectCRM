from django.shortcuts import render
from  crm import models
# Create your views here.


def dashboard(request):

    return render(request,'teacher/dashboard.html')


def my_classes(request):
    return render(request,'teacher/my_classes.html')


def view_class_stu_list(request,class_id):

    class_obj = models.ClassList.objects.get(id=class_id)
    return render(request,'teacher/class_stu_list.html',{'class_ojb':class_obj})