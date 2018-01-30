#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Shnu_course


def run(keywords_input):
    course_helper = Shnu_course.CourseHelper()

    course_utility = Shnu_course.CourseUtility()

    course_list = []

    keywords = [keywords_input]

    for course in course_helper.get_all_page_courses():
        for my_place in course.places:
            if course_utility.condition_keys(my_place.place, keywords):
                replace_course = course
                replace_course.places = [my_place]
                course_list.append(replace_course)

    chart = Shnu_course.CourseTable(course_list)

    return chart.echo_json()
