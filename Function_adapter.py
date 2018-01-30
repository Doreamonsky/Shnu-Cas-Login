#!/usr/bin/python
# -*- coding: UTF-8 -*-

def run(module_type, keyword):
    if module_type == 'courses_by_keywords':
        import Shnu_course_table
        return Shnu_course_table.run(keyword)
    if module_type == 'courses_by_classroom_keywords':
        import Shnu_classroom
        return Shnu_classroom.run(keyword)
    if module_type == 'courses_by_id':
        import Shnu_course_table_by_id
        return Shnu_course_table_by_id.run(keyword)
