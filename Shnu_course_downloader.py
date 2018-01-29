#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib
import urllib2
import re
from bs4 import BeautifulSoup

def resatisfy(myStr):
    newStr = myStr.replace('\n','')
    newStr = newStr.replace(',','<br>')
    newStr = newStr.encode('utf-8')
    return newStr


#curl 'http://course.shnu.edu.cn/eams/stdSyllabus!search.action?lesson.project.id=1&lesson.semester.id=102&_=1516424382052' \
# -XGET \
# -H 'Referer: http://course.shnu.edu.cn/eams/stdSyllabus!search.action?lesson.project.id=1&lesson.semester.id=102' \
# -H 'Host: course.shnu.edu.cn' \
# -H 'Accept: text/html, */*; q=0.01' \
# -H 'Connection: keep-alive' \
# -H 'Accept-Language: en-us' \
# -H 'Accept-Encoding: gzip, deflate' \
# -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7' \
# -H 'Cookie: semester.id=102; JSESSIONID=49A9D01DF22147DC0FBA5E43AF507F1B; UM_distinctid=15db6a68e559ec-02ca7b47fac51c-1d401925-232800-15db6a68e56927' \
# -H 'X-Requested-With: XMLHttpRequest'

course_url = "http://course.shnu.edu.cn/eams/stdSyllabus!search.action?lesson.project.id=1&lesson.semester.id=142"

url_opner = urllib2.build_opener()

value = {"pageNo":1}

response = url_opner.open(course_url, urllib.urlencode(value))

webText = response.read()

my = re.compile('pageInfo\(\d,(\d+),(\d+)\)')

content_per_page = my.findall(webText)[0][0]
content_length = my.findall(webText)[0][1]

page_for_timer = int(int(content_length)/int(content_per_page))

for i in range(1,page_for_timer):
    print i

    value = {"pageNo":i}

    response = url_opner.open(course_url,urllib.urlencode(value))

    webText = response.read()

    web_soup = BeautifulSoup(webText, 'lxml')


    match_pattern = re.compile("'(\d+)']='(.*)';")

    time_table ={}

    for group in re.findall(match_pattern,webText):
        time_table[str(group[0])] = str(group[1])

    data_list = []

    file_object = open('data/semester201702/course_page{0}.txt'.format(i), 'w')

    for idx, tr in enumerate(web_soup.find_all('tr')):
        if idx != 0:
            tds = tr.find_all('td')
            if len(tds)>0:
                class_and_teacher = "no place"
                class_id = str(tds[0].input['value'])

                if time_table.has_key(class_id):
                    if class_and_teacher:
                        class_and_teacher = time_table[class_id]
                    else:
                        class_and_teacher = "no place"

                data = "{0}${1}${2}${3}${4}${5}${6}${7}${8}${9}${10} \n".format(resatisfy(tds[1].text),
                                                       resatisfy(tds[2].text),
                                                       resatisfy(tds[3].text),
                                                       resatisfy(tds[4].text),
                                                       resatisfy(tds[5].text),
                                                       resatisfy(tds[6].text),
                                                       resatisfy(tds[7].text),
                                                       resatisfy(tds[8].text),
                                                       resatisfy(tds[9].text),
                                                       resatisfy(tds[10].text),
                                                       class_and_teacher)
                file_object.write(data)

    file_object.close()

