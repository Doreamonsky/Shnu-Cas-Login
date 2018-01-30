#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Shnu_course_table
import Shnu_classroom
import Shnu_course_table_by_id


class MyAdapter:
    def __init__(self):
        print 'MyAdapter'

    def run(self, module_type, keyword):
        if module_type == 'courses_by_keywords':
            return Shnu_course_table.ShnuCourseTable().run(keyword)
        if module_type == 'courses_by_classroom_keywords':
            return Shnu_classroom.ShnuClassroom().run(keyword)
        if module_type == 'courses_by_id':
            return Shnu_course_table_by_id.ShnuCourseTableByID().run(keyword)
