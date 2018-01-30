#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Shnu_course


def run(keywords_input):
    keywords = keywords_input.split(',')

    course_helper = Shnu_course.CourseHelper()

    course_utility = Shnu_course.CourseUtility()

    course_list = []

    for course in course_helper.get_all_page_courses():
        if course_utility.condition_keys(course.for_class, keywords) and len(course_list) < 30:
            course_list.append(course)

    my_course_table = Shnu_course.CourseTable(course_list)

    return my_course_table.echo_json()
