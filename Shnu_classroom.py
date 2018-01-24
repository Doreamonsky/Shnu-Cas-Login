#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Shnu_course

course_helper = Shnu_course.CourseHelper()

course_utility = Shnu_course.CourseUtility()

course_list = []

keywords = ['奉贤5教楼A207']


for course in course_helper.get_all_page_courses():
    for my_place in course.places:
        if course_utility.condition_keys(my_place.place,keywords):
            replace_course = course
            replace_course.places = [my_place]
            course_list.append(replace_course)


chart = Shnu_course.CourseTable (course_list)
chart.echo_chart()