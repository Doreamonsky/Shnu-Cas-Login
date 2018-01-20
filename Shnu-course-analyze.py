import Shnu_course

course_helper = Shnu_course.CourseHelper()

for course in course_helper.get_page_courses(60):
    print '####'
    print course.course_id
    print course.course_name
    print course.course_teacher
    print '####'

