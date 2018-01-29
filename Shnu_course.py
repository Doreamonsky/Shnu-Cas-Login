#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv
import re
import os
import json

from prettytable import PrettyTable
import prettytable

folder = 'semester201702'


# 课程教室地点数据
class CoursePlace:
    def __init__(self, data):
        self.teacher = data[0]
        self.week = data[1]
        self.time = data[2]
        self.week_duration = data[3]
        self.place = data[4]


# 课程数据
class Course:
    def __init__(self, c_id, c_name, c_type, c_class, c_teacher, c_a_number, c_m_number, c_score, c_all_duration,
                 c_week_duration, c_places):
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


# 课程获取
class CourseHelper:
    def __init__(self):
        self.started = True

    def get_page_courses(self, page_id):
        csv_reader = csv.reader(file('data/{0}/course_page{1}.txt'.format(folder, page_id)), delimiter='$')
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

        i = 1

        while os.path.exists('data/{0}/course_page{1}.txt'.format(folder, i)):
            all_course_list += self.get_page_courses(i)
            i += 1

        return all_course_list

    def get_course_place(self, place_str):  # 毛红娟 星期一 8-9 [1-16]  奉贤4教楼A219  <br>王敏 星期二 1-2 [1-16]  奉贤4教楼A311

        place_str = place_str.replace('<br>', '')  # 防止干扰正则

        course_place_list = []

        # 每周都有的课程
        place_pattern = re.compile(
            "(\S+)\s+(星期\S+)\s+(\d+\-\d+)\s+(\S+)\s+(\S+)")  # \S+ 匹配非空字符 \s+ 空字符

        for group in place_pattern.findall(place_str):
            my_place = CoursePlace(
                group
            )

            course_place_list.append(my_place)

        return course_place_list


# 课程表生成
class CourseUtility:
    def condition_keys(self, str_to_check, key_words):
        valid = True

        for key_world in key_words:
            # 过滤搜索
            if '/' in key_world:
                replaced_key_word = key_world.replace('/', '')
                if replaced_key_word in str_to_check:
                    valid = False
            # 括号不允许
            elif '?' in key_world:
                if '(' in str_to_check or '（' in str_to_check:
                    valid = False
            # 正常搜索
            else:
                if key_world not in str_to_check:
                    valid = False

        return valid


class CourseTable:

    def covert_class_time(self, time):
        start = time.split('-')[0]
        end = time.split('-')[1]
        return range(int(start) - 1, int(end), 1)  # 对齐课表

    def convert_week(self, week):
        if week == '星期一':
            return 'Mon'
        elif week == '星期二':
            return 'Tue'
        elif week == '星期三':
            return 'Wed'
        elif week == '星期四':
            return 'Thus'
        elif week == '星期五':
            return 'Fri'

    # t 存[课程，地点】
    ct_data = {
        'Mon': ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10', 't11', 't12', 't13', 't14', 't15'],
        'Tue': ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10', 't11', 't12', 't13', 't14', 't15'],
        'Wed': ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10', 't11', 't12', 't13', 't14', 't15'],
        'Thus': ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10', 't11', 't12', 't13', 't14', 't15'],
        'Fri': ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10', 't11', 't12', 't13', 't14', 't15']
    }

    # 输出数据
    ct_out = {
        'Mon': ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10', 't11', 't12', 't13', 't14', 't15'],
        'Tue': ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10', 't11', 't12', 't13', 't14', 't15'],
        'Wed': ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10', 't11', 't12', 't13', 't14', 't15'],
        'Thus': ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10', 't11', 't12', 't13', 't14', 't15'],
        'Fri': ['t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 't10', 't11', 't12', 't13', 't14', 't15']
    }

    # 将课程数据暂存在ct中
    def __init__(self, course_list):
        for my_course in course_list:
            for my_place in my_course.places:
                time_occupied_by_class = self.covert_class_time(my_place.time)

                for i in time_occupied_by_class:
                    if self.ct_data.has_key(self.convert_week(my_place.week)):
                        if 't' not in self.ct_data[self.convert_week(my_place.week)][i]:
                            self.ct_data[self.convert_week(my_place.week)][i].append([my_course, my_place])
                        else:
                            self.ct_data[self.convert_week(my_place.week)][i] = [[my_course, my_place]]

    def echo_chart(self):
        # table = PrettyTable()
        #
        # table.add_column('time', ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'])
        #
        # table.hrules = prettytable.ALL
        #
        # for week, time_array in self.ct_data.items():
        #
        #     for index in range(0, len(time_array)):
        #         if 't' not in time_array[index]:
        #             item = time_array[index]
        #             self.ct_out[week][index] = '课程:{0} \n 教室:{1} \n 教师: {2} \n 时间：{3}'.format(item[0].name, item[1].place,
        #                                                                             item[1].teacher,item[1].week_duration)
        #
        #
        #
        # for t in ["Mon", "Tue", "Wed", "Thus", "Fri"]:
        #     table.add_column(t, self.ct_out[t])
        #
        # print table.get_string()
        print '业务调整，请到小程序得到Chart'

    def echo_json(self):
        json_str = json.dumps(self.ct_data, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        print json_str
