#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Shnu_course


def run(keywords_input):
    course_id_list = keywords_input.split(',')

    course_list = []

    course_helper = Shnu_course.CourseHelper()

    for course in course_helper.get_all_page_courses():
        if course.id in course_id_list:
            course_list.append(course)

    course_table = Shnu_course.CourseTable(course_list)

    return course_table.echo_json()
