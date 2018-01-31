#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Shnu_course_table
import Shnu_classroom
import Shnu_course_table_by_id
import Shnu_courses_by_keywords


class MyAdapter:
    def __init__(self):
        print 'MyAdapter'

    def run(self, module_type, keywords):
        if module_type == 'courses_by_keywords':
            return Shnu_course_table.ShnuCourseTable().run(keywords)
        if module_type == 'courses_by_classroom_keywords':
            return Shnu_classroom.ShnuClassroom().run(keywords)
        if module_type == 'courses_by_id':
            return Shnu_course_table_by_id.ShnuCourseTableByID().run(keywords)
        if module_type == 'courses_list_by_keywords':
            return Shnu_courses_by_keywords.ShnuCoursesByKeywords().run(keywords)
