#_*_coding:utf-8_*_

from django import forms

class ApprovalForm(forms.Form):
    comment = forms.CharField(label="你的审批意见",widget=forms.Textarea(attrs={'class': "form-control"}))
    status_choices = ((0, '同意'), (1, '拒绝'))
    status = forms.IntegerField(label="审批结果",widget=forms.widgets.Select(choices=status_choices,
                                                                  attrs={'class': "form-control"}))

