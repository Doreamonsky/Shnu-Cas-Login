#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Shnu_course

course_helper = Shnu_course.CourseHelper()

for course in course_helper.get_page_courses(60):
    print '####'
    print course.name

    print course.places[0].week
    print course.places[0].time
    print course.places[0].week_duration
    print course.places[0].teacher
    print course.places[0].place


    print '####'

