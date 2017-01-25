#_*_coding:utf-8_*_

from crm import models
from django import forms

from crm.king_admin_old.admin_base import ModelAdminBase,register


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
    fk_fields = ('school','course_grade')

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

class CourseRecordAdmin(ModelAdminBase):
    model = models.CourseRecord
    list_display = ('course','day_num','date','teacher','has_homework','homework_title','study_records')
    fk_fields = ('course','teacher')
    list_filter = ('course','teacher','has_homework','day_num')
    def study_records(self):
        ele = '''<a class="btn-link" href='/kingadmin/crm_studyrecord/?&course_record=%s' >学员成绩</a>''' \
              %(self.instance.id)

        return ele
    study_records.display_name = "学员学习记录"

class StudyRecordAdmin(ModelAdminBase):
    model = models.StudyRecord
    list_display = ('student','course_record','record','score','date','note')
    list_filter = ('student','course_record')
    choice_fields = ('record','score')
    fk_fields = ('student','course_record')





class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = models.UserProfile
        fields = ('email','name')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        if len(password1) < 6:
            raise forms.ValidationError("Passwords takes at least 6 letters")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserProfileAdmin(ModelAdminBase):
    add_form = UserCreationForm
    model =  models.UserProfile
    list_display = ('id','email','is_staff')
    readonly_fields = ['password',]

    filter_horizontal = ('user_permissions','roles')


class FirstLayerMenuAdmin(ModelAdminBase):
    model = models.FirstLayerMenu
    list_display = ('id','url_type','url_name','order')
    choice_fields = ['url_type']

class RoleAdmin(ModelAdminBase):
    model = models.Role
    list_display = ('name',)
    filter_horizontal = ('menus',)

register(enabled_admins,CustomerAdmin)
register(enabled_admins,ClasslistAdmin)
register(enabled_admins,EnrollmentAdmin)
register(enabled_admins,PaymentRecordAdmin)
register(enabled_admins,CourseRecordAdmin)
register(enabled_admins,StudyRecordAdmin)
register(enabled_admins,UserProfileAdmin)
register(enabled_admins,FirstLayerMenuAdmin)
register(enabled_admins,RoleAdmin)