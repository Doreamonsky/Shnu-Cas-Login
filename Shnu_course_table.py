#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Shnu_course
import sys, getopt
import json


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hsk:t:", ["keyword=", "type="])
    except getopt.GetoptError:
        print 'getopt.GetoptError'
        exit()

    is_json = False
    is_sever = False

    keywords_input = []
    keywords_data = ''

    for opt, arg in opts:
        if opt == '-h':
            print 'Shnu_course_table.py -k <keyword> -t <type> json or table -s'
            exit()
        elif opt == "-s":
            is_sever = True
        elif opt in ("-k", "--keyword"):
            keywords_input = arg.split(',')
        elif opt in ("-t", "--type"):
            is_json = arg == 'json'


    if len(keywords_input) <= 0:
        print 'Usage: Python Shnu_course_table.py -k <keyword> -t <type> json or table'
        exit()


    course_helper = Shnu_course.CourseHelper()

    course_utility = Shnu_course.CourseUtility()

    course_list = []

    for course in course_helper.get_all_page_courses():
        if course_utility.condition_keys(course.for_class, keywords_input):
            course_list.append(course)

            if not is_sever:
                print course.for_class

    my_course_table = Shnu_course.CourseTable(course_list)

    if is_json:
        my_course_table.echo_json()
    else:
        my_course_table.echo_chart()


if __name__ == "__main__":
    main(sys.argv[1:])
