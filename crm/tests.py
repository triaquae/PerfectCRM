from django.test import TestCase
from crm import models
import random
# Create your tests here.



class CustomerEnrollmentTestCase(TestCase):

    def test_customer_create(self):
        user  = models.UserProfile.objects.create(
            email='alex@126.com',
            name= 'Alex Li'
        )

        course = models.Course.objects.create(
            name='python',
            description='python test',
            outline='dddd',
            period=3
        )
        new_customer = models.Customer.objects.create(
            qq = 121423,
            consultant_id = user.id,
            course_id=course.id

        )


        new_customer.status = 1
        new_customer.save()


