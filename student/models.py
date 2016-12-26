from django.db import models

from crm.models import UserProfile,Customer
# Create your models here.



class Account(models.Model):
    account = models.OneToOneField(UserProfile,related_name="stu_account")
    profile = models.OneToOneField(Customer)





