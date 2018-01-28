#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Shnu_course
import sys, getopt


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hsk:t:", ["keyword=", "type="])
    except getopt.GetoptError:
        print 'getopt.GetoptError'
        exit()

    for opt, arg in opts:
        if opt == '-h':
            print 'Shnu_classroom.py -k <keyword> -t <type> json or table -s'
            exit()
        elif opt in ("-k", "--keyword"):
            keywords_input = arg.split(',')


    course_helper = Shnu_course.CourseHelper()

    course_utility = Shnu_course.CourseUtility()

    course_list = []

    keywords = keywords_input

    for course in course_helper.get_all_page_courses():
        for my_place in course.places:
            if course_utility.condition_keys(my_place.place, keywords):
                replace_course = course
                replace_course.places = [my_place]
                course_list.append(replace_course)

    chart = Shnu_course.CourseTable(course_list)

    chart.echo_json()


if __name__ == "__main__":
    main(sys.argv[1:])
