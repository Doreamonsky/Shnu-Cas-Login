#!/usr/bin/python
# -*- coding: UTF-8 -*-

import urllib2
import urllib
import cookielib
import re
import time

from bs4 import BeautifulSoup


def resatisfy(myStr):
    if len(myStr) == 0:
        myStr = 'Null-Data'

    newStr = myStr.replace('\n', '')
    newStr = newStr.replace(',', '<br>')
    newStr = newStr.encode('utf-8')
    return newStr




# curl 'http://course.shnu.edu.cn/eams/stdSyllabus!search.action' \
# -XPOST \
# -H 'Referer: http://course.shnu.edu.cn/eams/stdSyllabus!search.action' \
# -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
# -H 'Origin: http://course.shnu.edu.cn' \
# -H 'Host: course.shnu.edu.cn' \
# -H 'Accept: */*' \
# -H 'Connection: keep-alive' \
# -H 'Accept-Language: en-us' \
# -H 'Accept-Encoding: gzip, deflate' \
# -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7' \
# -H 'Cookie: semester.id=142; JSESSIONID=A5FC3E66E452452BFC10241988953968' \
# -H 'Content-Length: 253' \
# -H 'X-Requested-With: XMLHttpRequest' \
# --data 'lesson.no=&lesson.course.name=&lesson.courseType.name=&lesson.teachClass.name=&teacher.name=&lesson.teachClass.stdCount=&lesson.teachClass.limitCount=&lesson.course.credits=&lesson.coursePeriod=&lesson.project.id=1&lesson.semester.id=142&_=1520143201745'

def make_cookie(name, value): return cookielib.Cookie(version=0, name=name, value=value, port=None,
                                                      port_specified=False, domain="xxxxx", domain_specified=True,
                                                      domain_initial_dot=False, path="/", path_specified=True,
                                                      secure=False, expires=None, discard=False, comment=None,
                                                      comment_url=None, rest=None)


# CAS Temporary
homepage_url = 'http://cas.shnu.edu.cn/cas/login?service=http%3A%2F%2Fcourse.shnu.edu.cn%2Feams%2Flogin.action'
login_url = "http://cas.shnu.edu.cn/cas/login;jsessionid={0}?service=http%3A%2F%2Fcourse.shnu.edu.cn%2Feams%2Flogin.action"

username = raw_input("UserName")
password = raw_input("Password")

JSESSIONID = ''  # 打开cas后分配的

# Cookies
my_cookies = cookielib.CookieJar()

my_cookies.set_cookie(make_cookie('semester.id', '142;'))
cookie_pr = urllib2.HTTPCookieProcessor(my_cookies)
url_opener = urllib2.build_opener(cookie_pr)

# 访问Cas获得 JSESSIONID It 与 execution
response = url_opener.open(homepage_url)

for cookie in my_cookies:
    if cookie.name == "JSESSIONID":
        JSESSIONID = cookie.value

web_text = response.read().decode('utf-8')

matchpattern_lt = re.compile('LT-.*-cas')
result = re.findall(matchpattern_lt, web_text)
if result:
    lt = result[0]
else:
    print "not match"

matchpattern_ex = re.compile('e\ds\d')
result = re.findall(matchpattern_ex, web_text)

if result:
    ex = result[0]
else:
    print "not match"

login_url = login_url.format(JSESSIONID)

values = {
    '_eventId': 'submit',
    'code': 'code',
    'execution': ex,
    'lt': lt,
    'password': password,
    'phoneCode': 'submit',
    'type': 'submit',
    'username': username,
}

data = urllib.urlencode(values)

request = urllib2.Request(login_url, data)

response = url_opener.open(request)

for cookie in my_cookies:
    print "Cookies: {0}:{1}".format(cookie.name, cookie.value)

# Cas

course_url = "http://course.shnu.edu.cn/eams/stdSyllabus!search.action?lesson.project.id=1&lesson.semester.id=142"

value = {"pageNo": 1}

response = url_opener.open(course_url, urllib.urlencode(value))

webText = response.read()


my = re.compile('pageInfo\(\d,(\d+),(\d+)\)')

content_per_page = my.findall(webText)[0][0]
content_length = my.findall(webText)[0][1]

page_for_timer = int(int(content_length) / int(content_per_page))

time.sleep(1)


for i in range(44, 45):
    print i


    value = {"pageNo": i}

    response = url_opener.open(course_url, urllib.urlencode(value))

    webText = response.read()

    print webText

    web_soup = BeautifulSoup(webText, 'lxml')

    match_pattern = re.compile("'(\d+)']='(.*)';")

    time_table = {}

    for group in re.findall(match_pattern, webText):
        time_table[str(group[0])] = str(group[1])

    data_list = []

    file_object = open('data/semester201702/course_page{0}.txt'.format(i), 'w')

    for idx, tr in enumerate(web_soup.find_all('tr')):
        if idx != 0:
            tds = tr.find_all('td')
            if len(tds) > 0:
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

    time.sleep(0.5)

