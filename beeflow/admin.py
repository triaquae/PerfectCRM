from django.contrib import admin

from beeflow import models
# Register your models here.


class StepAdmin(admin.ModelAdmin):
    list_display = ['flow_template','name','order','role']
    list_filter = ['flow_template',]

class FlowRecordAdmin(admin.ModelAdmin):
    list_display = ['flow','step','user','status','date','comment']
    list_filter = ['flow','status']

admin.site.register(models.FlowTemplate)
admin.site.register(models.Flow)
admin.site.register(models.Step,StepAdmin)
admin.site.register(models.FlowRecord,FlowRecordAdmin)
admin.site.register(models.FlowRole)

admin.site.register(models._FlowBecome_Full_Staff)
admin.site.register(models._FlowLoan)
admin.site.register(models._FlowTrip)
admin.site.register(models._FlowVaction)
