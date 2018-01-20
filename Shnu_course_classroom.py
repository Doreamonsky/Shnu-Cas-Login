#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Shnu_course
from prettytable import PrettyTable

course_helper = Shnu_course.CourseHelper()

classroom_list = {'': []}

for course in course_helper.get_all_page_courses():
    for myplace in course.places:
        if classroom_list.has_key(myplace.place):
            classroom_list[myplace.place].append(course)
        else:
            classroom_list[myplace.place] = [course]

my_table = PrettyTable(['Class', 'ClassNumber', 'MaxCapacityPrediction'])

for key, value in classroom_list.items():
    number = 0

    for course in value:
        if course.max_number > number:
            number = course.max_number

    my_table.add_row([key, len(value), number])

print my_table.get_string(sortby='Class')
