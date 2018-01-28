#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Shnu_course
import json

course_helper = Shnu_course.CourseHelper()

classroom_list = {
    '奉贤1教': [],
    '奉贤2教': [],
    '奉贤3教': [],
    '奉贤4教': [],
    '奉贤5教': [],
    '徐汇一教': [],
    '徐汇二教': [],
    '徐汇三教': [],
    '徐汇四教': [],
    '徐汇五教': [],
    '徐汇六教': [],
    '徐汇计算中心': []
}

for building in classroom_list:
    for course in course_helper.get_all_page_courses():
        for myplace in course.places:
            if isinstance(myplace, Shnu_course.CoursePlace):
                if building in myplace.place:
                    if myplace.place not in classroom_list[building]:
                        classroom_list[building].append(myplace.place)



for keys in classroom_list.keys():
    classroom_list[keys] = sorted(classroom_list[keys])


file_object = open('data/classroom.txt', 'w')
file_object.write(json.dumps(classroom_list,sort_keys=True))
file_object.close()