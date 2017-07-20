from django.shortcuts import render
from beeflow import models
from django.contrib.auth.decorators import login_required
from beeflow import flows
from beeflow import forms

# Create your views here.


@login_required
def my_application(request):



    return render(request,"beeflow/my_application.html")

@login_required
def flow_detail(request,flow_id):
    flow_obj = models.Flow.objects.get(id=flow_id)
    return render(request,"beeflow/flow_detail.html", locals())


def my_approvals(request):
    """flows that needed to be approved by me """

    flow_manager_obj = flows.FlowManger(request)
    queued_flows = flow_manager_obj.get_assigned_to_me_flowlist()

    return render(request,"beeflow/my_approvals.html", locals())

def my_approval_records(request):
    """我的审批记录页"""


    return render(request,"beeflow/my_approval_records.html", locals())


def flow_examination(request,record_id):
    """流程审批页"""
    flow_record_obj = models.FlowRecord.objects.get(id=record_id)
    if request.method == "POST":
        form = forms.ApprovalForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            flow_record_obj.status = form.cleaned_data['status']
            flow_record_obj.user = request.user
            flow_record_obj.comment = form.cleaned_data['comment']
            flow_record_obj.save()
    else:
        form = forms.ApprovalForm()
    return render(request,"beeflow/flow_examination.html",locals())