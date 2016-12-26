#_*_coding:utf-8_*_

import datetime
import re
from django import template


from django.utils.safestring import mark_safe,mark_for_escaping
from  django.core.urlresolvers import reverse as url_reverse

register = template.Library()


@register.simple_tag
def get_study_record_count(enroll_obj):
    study_records = []
    course_records = enroll_obj.course_grade.courserecord_set.select_related()
    for obj in course_records:
        study_records.extend(obj.studyrecord_set.select_related().filter(student=enroll_obj.customer))
    return study_records

@register.simple_tag
def  get_course_score(study_records):
    score = 0
    for i in study_records:
        score += i.score
    return score


@register.simple_tag
def get_study_record(course_record,enroll_obj):
    study_record_obj = course_record.studyrecord_set.select_related().filter(student=enroll_obj.customer)
    if study_record_obj:
        return study_record_obj[0]
