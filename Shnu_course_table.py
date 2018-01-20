#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Shnu_course
import sys, getopt


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hk:t:", ["keyword=", "type="])
    except getopt.GetoptError:
        print 'Shnu_course_table.py -k <keyword> -t <type> json or table'
        exit()

    isJson = False

    keyworks_input = []

    for opt, arg in opts:
        if opt == '-h':
            print 'Shnu_course_table.py -k <keyword> -t <type> json or table'
            exit()
        elif opt in ("-k", "--keyword"):
            keyworks_input = arg.split(',')
        elif opt in ("-t", "--type"):
            isJson = arg == 'json'

    if len(keyworks_input) <= 0:
        print 'Usage: Python Shnu_course_table.py -k <keyword> -t <type> json or table'
        exit()

    course_helper = Shnu_course.CourseHelper()

    course_utility = Shnu_course.CourseUtility()

    course_list = []

    for course in course_helper.get_all_page_courses():
        if course_utility.condition_keys(course.for_class, keyworks_input):
            course_list.append(course)

            print course.for_class

    my_course_table = Shnu_course.CourseTable(course_list)

    if isJson:
        my_course_table.echo_json()
    else:
        my_course_table.echo_chart()


if __name__ == "__main__":
    main(sys.argv[1:])
