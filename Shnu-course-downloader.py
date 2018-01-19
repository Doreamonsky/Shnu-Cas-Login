#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib
import urllib2
import re
from bs4 import BeautifulSoup

def resatisfy(myStr):
    newStr = myStr.replace('\n','')
    newStr = newStr.encode('utf-8')
    return newStr

course_url = "http://course.shnu.edu.cn/eams/stdSyllabus!search.action"
for i in range(1,1166):
    print i

    value = {"pageNo":i}

    url_opner = urllib2.build_opener()
    response = url_opner.open(course_url,urllib.urlencode(value))


    webText = response.read()



    web_soup = BeautifulSoup(webText, 'lxml')



    match_pattern = re.compile("'(\d+)']='(.*)';")

    time_table ={}

    for group in re.findall(match_pattern,webText):
        time_table[str(group[0])] = str(group[1])

    #print time_table

    data_list = []





    file_object = open('data/course_page{0}.txt'.format(i), 'w')

    for idx, tr in enumerate(web_soup.find_all('tr')):
        if idx != 0:
            tds = tr.find_all('td')
            if len(tds)>0:
                # print tds[1].text
                # print tds[2].text
                # print tds[3].text
                # print tds[4].text
                # print time_table[str(tds[0].input['value'])]
                class_and_teacher = "no place"
                class_id = str(tds[0].input['value'])

                if time_table.has_key(class_id):
                    if class_and_teacher:
                        class_and_teacher = time_table[class_id]
                    else:
                        class_and_teacher = "no place"

                data = "{0},{1},{2},{3},{4} \n".format(resatisfy(tds[1].text),resatisfy(tds[2].text),resatisfy(tds[3].text),resatisfy(tds[4].text),class_and_teacher)
                file_object.write(data)

    file_object.close()

