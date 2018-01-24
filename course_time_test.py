#!/usr/bin/python
# -*- coding: UTF-8 -*-
import csv
import Shnu_course
import re

folder = 'semester201702'

helper = Shnu_course.CourseHelper
for page_id in range(1, 260):
    csv_reader = csv.reader(file('data/{0}/course_page{1}.txt'.format(folder, page_id)), delimiter=';')

    for line in csv_reader:
        place_str_list = line[10].split('<br>')

        for place_str in place_str_list:
            match = re.compile('(\S+)\s+(星期\S+)\s+(\d+\-\d+)\s+(\S+)\s+(\S+)')

            # for group in match.findall(place_str):
            #
            #     # for e in group:
            #     #     print e
            #     if '单' in group[3] or '双' in group[3]:
            #         print group[3]

            if len(match.findall(place_str)) == 0:
                if '单' in place_str or '双' in place_str:
                    print place_str
                    print page_id