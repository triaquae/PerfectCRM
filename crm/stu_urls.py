
from django.conf.urls import url,include
from crm import  stu_views as views

urlpatterns = [
    url(r'^$', views.my_courses, name="my_courses"),
    url(r'my_grade/$', views.my_grade, name="my_grade"),

]
