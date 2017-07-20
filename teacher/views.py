from django.shortcuts import render
from  crm import models
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def dashboard(request):

    return render(request,'teacher/dashboard.html')

@login_required
def my_classes(request):
    return render(request,'teacher/my_classes.html')

@login_required
def view_class_stu_list(request,class_id):

    class_obj = models.ClassList.objects.get(id=class_id)
    return render(request,'teacher/class_stu_list.html',{'class_ojb':class_obj})