#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

folder = 'semester201801'

i = 1

while os.path.exists('data/{0}/course_page{1}.txt'.format(folder, i)):
    print 'data/{0}/course_page{1}.txt'.format(folder, i)

    with open('data/{0}/course_page{1}.txt'.format(folder, i), 'r') as my_file_raw:
        lines = my_file_raw.readlines()

    with open('data/{0}/course_page{1}.txt'.format(folder, i), 'w') as my_file:
        for line in lines:
            if '&' in line:
                line = line.replace('&', '')
            my_file.write(line)

    i += 1
