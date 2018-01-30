#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Shnu_course_table
import Shnu_classroom
import Shnu_course_table_by_id


def run(module_type, keyword):
    if module_type == 'courses_by_keywords':
        return Shnu_course_table.run(keyword)
    if module_type == 'courses_by_classroom_keywords':
        return Shnu_classroom.run(keyword)
    if module_type == 'courses_by_id':
        return Shnu_course_table_by_id.run(keyword)
