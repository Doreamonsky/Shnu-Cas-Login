#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Shnu_course


course_helper = Shnu_course.CourseHelper()

for course in course_helper.get_all_page_courses():
    if '嵌入式系统' in course.name:
        print course.name

        for place in course.places:
            print '##### \n 老师：{0} 地点：{1}  时间:{2} {3} ID:{4} \n'.format(place.teacher,place.place,place.week,place.time,course.for_class)



