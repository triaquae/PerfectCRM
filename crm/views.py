from django.shortcuts import render,HttpResponseRedirect,Http404

from crm import forms
from crm import models
from crm import admin
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from  crm.king_admin.king_admin import enabled_admins
from crm.king_admin import tables
# Create your views here.

@login_required
def sales_dashboard(request):
    return render(request,'crm/dashboard.html')

@login_required
def customers(request):
    '''sales role home page'''
    print(request.GET)
    customer_list = models.Customer.objects.all()

    order_res = forms.get_orderby(request,customer_list,admin.CustomerAdmin)
    #print('----->',order_res)
    paginator = Paginator(order_res[0],admin.CustomerAdmin.list_per_page)

    page = request.GET.get('page')
    try:
        customer_objs = paginator.page(page)
    except PageNotAnInteger:
        customer_objs = paginator.page(1)
    except EmptyPage:
        customer_objs = paginator.page(paginator.num_pages)


    table_obj = forms.TableHandler(request,
                                   models.Customer,
                                   customer_objs,
                                   admin.CustomerAdmin,
                                   order_res)
    #print("list_filter",table_obj.list_filter)
    return render(request, "crm/customers.html", {"customer_table":table_obj,
                                                'paginator': paginator})
@login_required
def my_customers(request):
    '''每个销售自己的客户列表'''
    return render(request,"crm/my_customer.html")

@login_required
def sales_report(request):
    '''销售报表'''
    return render(request, "crm/sales_report.html")



def acc_login(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            request.session.set_expiry(60*60)
            return HttpResponseRedirect(request.GET.get("next") if request.GET.get("next") else "/")

        else:
            return render(request,'login.html',{'login_err': 'Wrong username or password!'})

    return render(request,'login.html')





def acc_logout(request):

    logout(request)
    return render(request,'login.html')



