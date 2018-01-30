# coding:utf-8

import urllib2
import urllib
import cookielib
import re

homepage_url = 'http://cas.shnu.edu.cn/cas/login?service=http%3A%2F%2Fcourse.shnu.edu.cn%2Feams%2Flogin.action'
login_url = "http://cas.shnu.edu.cn/cas/login;jsessionid={0}?service=http%3A%2F%2Fcourse.shnu.edu.cn%2Feams%2Flogin.action"
course_url = "http://course.shnu.edu.cn/eams/stdExamTable!examTable.action?examBatch.id=201";

username = raw_input("UserName")
password = raw_input("Password")

JSESSIONID = ''  # 打开cas后分配的

# Cookies
my_cookies = cookielib.CookieJar()
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

request = urllib2.Request(course_url)
response = url_opener.open(request)

file_object = open('KaoshiShijian.txt', 'w')
file_object.write(response.read())
file_object.close()

print "Done! Check the folder"
