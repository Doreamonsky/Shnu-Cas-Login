#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Shnu_course
import sys, getopt
import json


def main(argv):
    course_id_list = []

    try:
        opts, args = getopt.getopt(argv, "hk:", ["keyword="])
    except getopt.GetoptError:
        print 'getopt.GetoptError'
        exit()
    for opt, arg in opts:
        if opt == '-h':
            print ''
            exit()
        elif opt in ("-k", "--keyword"):
            course_id_list = arg.split(',')



    course_list = []

    course_helper = Shnu_course.CourseHelper()

    for course in course_helper.get_all_page_courses():
        if course.id in course_id_list:
            course_list.append(course)

    course_table = Shnu_course.CourseTable(course_list)

    course_table.echo_json()


if __name__ == "__main__":
    main(sys.argv[1:])
