#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Shnu_course


class ShnuClassroom:
    def __init__(self):
        print 'ShnuClassroom'

    def run(self, keywords_input):
        course_helper = Shnu_course.CourseHelper()

        course_utility = Shnu_course.CourseUtility()

        course_list = []

        keywords = [keywords_input]

        print keywords
        print len(course_list)

        for course in course_helper.get_all_page_courses():
            for my_place in course.places:
                if course_utility.condition_keys(my_place.place, keywords):
                    course_list.append(Shnu_course.Course(
                        course.id, course.name, course.type, course.for_class, course.teacher,
                        course.actual_number, course.max_number, course.score, course.all_duration,
                        course.week_duration,
                        [my_place]
                    ))

        chart = Shnu_course.CourseTable(course_list)

        return chart.echo_json()
