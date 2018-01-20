import csv
import re

class Course:
    def __init__(self, c_id, c_name,c_type,c_class,c_teacher,c_a_number,c_m_number, c_score,c_duration,c_places):
        self.course_id = c_id
        self.course_name = c_name
        self.course_type = c_type
        self.course_class = c_class
        self.course_teacher = c_teacher
        self.course_actual_number = c_a_number
        self.course_max_number = c_m_number
        self.course_score = c_score
        self.course_duration = c_duration
        self.course_places = c_places



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
                line[9]
            )
            my_course_list.append(my_course)

        return my_course_list

    def get_all_page_courses(self):
        all_course_list = []
        for i in range(1,1167):
            all_course_list += self.get_page_courses(i)

        return all_course_list

    # def get_course_place(self,place_str):
    #     place_pattern = re.compile("/w+")