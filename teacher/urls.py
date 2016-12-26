
from django.conf.urls import url,include
from teacher import  views

urlpatterns = [
    url(r'^$', views.dashboard, name="teacher_dashboard"),

]
