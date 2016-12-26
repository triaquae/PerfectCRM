#_*_coding:utf-8_*_

from crm import models
from django import forms

from crm.king_admin.admin_base import ModelAdminBase,register


enabled_admins = {} #不要动，所有注册的表都会自动添加到这里


class CustomerAdmin(ModelAdminBase):
    model = models.Customer
    list_display = ['qq','qq_name','name','source','consultant','status','date','enroll']

    fk_fields = ('consultant',)
    choice_fields = ('source','status')
    list_filter = ('source','consultant','status')
    readonly_fields = ('consultant','status')
    search_fields = ('qq','consultant__email')
    colored_fields = {
        'status':{'已报名':"rgba(145, 255, 0, 0.78)",
                  '未报名':"#ddd"},
    }

    def enroll(self):
        '''报名'''
        print("customize field enroll",self)
        link_name = "报名"
        if self.instance.status == "signed":
            link_name = "报名新课程"
        return '''<a class="btn-link" href="/crm/enrollment/%s/">%s</a> ''' % (self.instance.id,link_name)
    enroll.display_name = "报名链接"

class EnrollmentAdmin(ModelAdminBase):
    model = models.Enrollment
    list_display = ['customer','school','course_grade','contract_agreed','contract_approved','enrolled_date']

class ClasslistAdmin(ModelAdminBase):
    model = models.ClassList
    list_display = ('branch','course','semester','start_date')
    fk_fields = ('branch','course')
    filter_horizontal = ('teachers',)
    default_actions = ['delete_selected','dd秀d']
    readonly_table = True

class PaymentRecordAdmin(ModelAdminBase):
    model = models.PaymentRecord
    list_filter = ('pay_type','date','consultant')
    list_display = ('id','enrollment','pay_type','paid_fee','date','consultant')
    fk_fields = ('enrollment','consultant')
    choice_fields = ('pay_type')

register(enabled_admins,CustomerAdmin)
register(enabled_admins,ClasslistAdmin)
register(enabled_admins,EnrollmentAdmin)
register(enabled_admins,PaymentRecordAdmin)