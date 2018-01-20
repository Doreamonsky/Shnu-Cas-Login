#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Shnu_course

course_helper = Shnu_course.CourseHelper()

course_utility = Shnu_course.CourseUtility()

keyworks_input = raw_input('输入关键词数组 用,分割').split(',')
course_list = []

for course in course_helper.get_all_page_courses():
    if course_utility.condition_keys(course.for_class, keyworks_input):
        course_list.append(course)

        print course.for_class

my_CourseTable = Shnu_course.CourseTable(course_list)

my_CourseTable.echo_chart()

my_CourseTable.echo_json()