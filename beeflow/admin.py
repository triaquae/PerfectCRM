from django.contrib import admin

from beeflow import models
# Register your models here.


admin.site.register(models.FlowTemplate)
admin.site.register(models.Flow)
admin.site.register(models.Step)
admin.site.register(models.FlowRecord)
admin.site.register(models.FlowRole)

admin.site.register(models._FlowBecome_Full_Staff)
admin.site.register(models._FlowLoan)
admin.site.register(models._FlowTrip)
admin.site.register(models._FlowVaction)
