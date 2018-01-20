#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv
import re

class CoursePlace:
    def __init__(self,teacher,week,time,week_duration,place):
        self.teacher = teacher
        self.week = week
        self.time = time
        self.week_duration = week_duration
        self.place = place



class Course:
    def __init__(self, c_id, c_name,c_type,c_class,c_teacher,c_a_number,c_m_number, c_score,c_all_duration,c_week_duration,c_places):
        self.id = c_id
        self.name = c_name
        self.type = c_type
        self.for_class = c_class
        self.teacher = c_teacher
        self.actual_number = c_a_number
        self.max_number = c_m_number
        self.score = c_score
        self.all_duration = c_all_duration
        self.week_duration = c_week_duration
        self.places = c_places



class CourseHelper:
    def __init__(self):
        print "Init Course system"

    def get_page_courses(self,page_id):
        csv_reader = csv.reader(file('data/course_page{0}.txt'.format(page_id)),delimiter=';')
        my_course_list = []

        for line in csv_reader:
            my_course = Course(
                line[0],
                line[1],
                line[2],
                line[3],
                line[4],
                line[5],
                line[6],
                line[7],
                line[8],
                line[9],
                self.get_course_place(line[10])
            )
            my_course_list.append(my_course)

        return my_course_list

    def get_all_page_courses(self):
        all_course_list = []
        for i in range(1,1167):
            all_course_list += self.get_page_courses(i)

        return all_course_list


    def get_course_place(self,place_str):    #毛红娟 星期一 8-9 [1-16]  奉贤4教楼A219  <br>王敏 星期二 1-2 [1-16]  奉贤4教楼A311

        place_str = place_str.replace('<br>','|') #防止干扰正则

        course_place_list = []

        place_pattern = re.compile("(\S+)\s(\S+)\s(\d)\-(\d)\s\[(\d+)\-(\d+)\]\s+(\S+)") #\S+ 匹配非空字符 \s+ 空字符

        for group in place_pattern.findall(place_str):
            my_place = CoursePlace(
                group[0],
                group[1],
                "{0}-{1}".format(group[2],group[3]),
                "{0}-{1}".format(group[4],group[5]),
                group[6]
            )

            course_place_list.append(my_place)

        return course_place_list

