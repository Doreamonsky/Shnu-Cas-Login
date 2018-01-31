#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Shnu_course
import json


class ShnuCoursesByKeywords:
    def __init__(self):
        self.course_list = []

    def run(self, keywords):

        keywords_list = keywords.split(',')
        course_utility = Shnu_course.CourseUtility()
        course_helper = Shnu_course.CourseHelper()

        for course in course_helper.get_all_page_courses():
            if course_utility.condition_keys(course.name, keywords_list) and len(self.course_list) < 50:
                self.course_list.append(course)

        json_str = json.dumps(self.course_list, default=lambda o: o.__dict__, sort_keys=True, indent=4)

        return json_str
