import sys
import json

class School(object):
    def __init__(self,school_name,address):
        self.school_name = school_name
        self.addess = address

    def create_class(self):
        print("欢迎创建班级".center(50, '-'))
        classroom_name = input("请输入班级名称:")
        classroom_period = input("请输入班级周期:")
        classroom_obj = Classroom(classroom_name, classroom_period, choice_school_obj.school_name)  # 班级的实例
        print("班级成功创建,班级信息如下".center(50, '-'))
        classrooms[classroom_name] = classroom_obj  # 将班级名与班级对象相关联
        classroom_obj.show_classroom_info()

    def hire_teacher(self):
        print("欢迎雇用讲师".center(50, '-'))
        teacher_name = input("请输入讲师名字:")
        teacher_sex = input("请输入讲师性别:")
        teacher_age = input("请输入讲师年龄:")
        teacher_course = input("请输入讲师对应课程:")
        teacher_classroom = input("请输入讲师对应班级:")
        teacher = Teacher(teacher_name, teacher_sex, teacher_age, teacher_course,
                          teacher_classroom, choice_school_obj.school_name)  # 实例化讲师对象
        teacher_dict = {"teacher_shcool_name": teacher.teacher_school_name, "teacher_sex": teacher_sex,
                        "teacher_age": teacher_age, "teacher_course": teacher_course,
                        "teacher_classroom": teacher_classroom}  # 用字典来存放讲师信息

        teacher.show_teacher_info()
        if not dic:  # 字典如果为空
            dic[teacher_name] = teacher_dict  # 将讲师名与讲师对象相关联
            # 通过json将讲师的字典序列化到teacher_文件中
            json.dump(dic, open("teacher_db", "w", encoding='utf-8'),
                      ensure_ascii=False, indent=2)
        else:  # 如果文件中已有讲师信息
            if dic.get(teacher_name):  # 字典中不存在key，则返回none,不曝错
                print("%s讲师已存在,不能创建名字相同的讲师" % teacher_name)
                flag = True
            elif not dic.get(teacher_name):
                dic[teacher_name] = teacher_dict
                json.dump(dic, open("teacher_db", "w", encoding='utf-8'), ensure_ascii=False, indent=2)

    def create_course(self):  #创建课程
        print("迎欢创建课程".center(50, '-'))
        course_type = input("请输入课程类型[eg:技术/教育/自然科学/艺术...]:")
        course_name = input("请输入课程名称:")
        course_price = input("请输入课程价格:")
        course_period = input("请输入课程周期:")
        course = Course(course_type, course_name, course_price, course_period, choice_school_obj.school_name)
        print("课程成功创建,课程信息如下".center(50, '-'))
        courses_dict[course_name] = course  # 将课程名与课程对象相关联
        course.show_course_info()





class Course(object):

    def __init__(self,course_type,course_name,course_price,course_period,course_place):
        self.course_type = course_type
        self.course_name = course_name
        self.course_price = course_price
        self.course_period = course_period
        self.course_place = course_place

    def show_course_info(self):
        print("课程类型:%s,名称:%s,价格:%s,周期:%s"%(self.course_type,self.course_name,self.course_price,self.course_period))


class Classroom(object):
    def __init__(self,classroom_name,classroom_period,class_school_name):
        self.classroom_name = classroom_name
        self.classroom_period = classroom_period
        self.classroom_school_name = class_school_name


    def show_classroom_info(self):
        print("班级名称:%s\n班级周期:%s" %(self.classroom_name,self.classroom_period))

class SchoolMenber(object):
    def __init__(self,member_name,member_sex,member_age):
        self.member_name = member_name
        self.member_sex = member_sex
        self.member_age = member_age


class Student(SchoolMenber):

    def __init__(self,stu_school,stu_name,stu_sex,stu_id,stu_age,stu_course,course_price):
        super(Student,self).__init__(stu_name,stu_sex,stu_age)
        self.stu_school = stu_school
        self.stu_name = stu_name
        self.stu_sex = stu_sex
        self.stu_id = stu_id
        self.stu_course = stu_course
        self.course_price = course_price

    def show_student_info(self):
         print("""
        ---------------学生%s的信息--------------
        Name:%s
        School:%s
        Sex:%s
        Age:%s
        ID:%s
        Course:%s
        Course_price:%s
        """ % (stu1.member_name,stu1.member_name,stu1.stu_school,stu1.member_sex,
               stu1.member_age, stu1.stu_id, stu1.stu_course,stu1.course_price))


class Teacher(SchoolMenber):
    def __init__(self, teacher_name, teacher_sex, teacher_age, teacher_course, teacher_classroom, teacher_school_name):
        super(Teacher, self).__init__(teacher_name, teacher_sex, teacher_age)
        self.teacher_course = teacher_course
        self.teacher_classroom = teacher_classroom
        self.teacher_school_name = teacher_school_name

    def show_teacher_info(self):
        print("""
        -------------讲师%s的信息-------------
        Name:%s
        Sex:%s
        Age:%s
        Course:%s
        Classroom:%s
        School_name:%s
        """ % (self.member_name, self.member_name, self.member_sex, self.member_age,
                                   self.teacher_course, self.teacher_classroom, self.teacher_school_name))
    def show_classroom(self, te_name):    #查看班级信息   传一个班级对象，通过对象查看班级信息
        class_room = Classroom(teachers_dict[te_name].teacher_classroom,
                               courses_dict[teachers_dict[te_name].teacher_course].course_period,
                               choice_school_obj.school_name)
        class_room.show_classroom_info()

    def show_student(self):     #查看学生信息    传一个学生对象，通过对象查看学生信息
        stu_name = input("请输入要查看学生名字:")
        stu_dict[stu_name].show_student_info()

def stu_regiest():  # 学生注册方法，目的是为了生成学生对象
    global stu1          #定义学生变量为全局变量
    stu_name = input("请输入学生姓名:")
    stu_sex = input("请输入学生性别:")
    stu_age = input("请输入学生年龄:")
    stu_id = input("请输入学生序号")
    print("1.%s[%sRMB], 2.%s[%sRMB], 3.%s[%sRMB], 4.返回" % (course1.course_name, course1.course_price,
                                                           course2.course_name, course2.course_price,
                                                           course3.course_name, course3.course_price))
    while True:
        course_num = input("请选择课程:")
        if course_num == '1':
            stu_course = course1.course_name
            stu1 = Student(choice_school_obj.school_name, stu_name, stu_sex,
                           stu_age, stu_id, stu_course,course1.course_price)
            stu_dict[stu_name] = stu1
            break
        elif course_num == '2':
            stu_course = course2.course_name
            stu1 = Student(choice_school_obj.school_name, stu_name, stu_sex,
                           stu_age, stu_id, stu_course, course2.course_price)
            stu_dict[stu_name] = stu1
            break
        elif course_num == '3':
            stu_course = course3.course_name
            stu1 = Student(choice_school_obj.school_name, stu_name, stu_sex,
                           stu_age, stu_id, stu_course, course3.course_price)
            #stu_school,stu_name,stu_sex,stu_age,stu_course,course_price
            stu_dict[stu_name] = stu1
            break
        elif course_num == '4':
            break
        else:
            continue
    stu1.show_student_info()

def students_view():      #学员视图
    while True:
        print("1.欢迎注册\n"
              "2.返回\n"
              "3.退出")
        num = input("请选择:")
        if num == '1':
            stu_regiest()        #调用学生注册方法并生成学生对象
        elif num == '2':
            break
        elif num == '3':
            sys.exit()
        else:
            continue


def teacher_view():     #讲师视图
    name = input("请输入讲师姓名:")
    while True:
        if dic.get(name) or teachers_dict.get(name):
            print("欢迎%s讲师".center(50, '-') % name)
        elif not dic.get(name) and not teachers_dict.get(name):
            print("%s讲师不存在" % name)
            break
        print("1.查看班级\n"
              "2.查看学员信息\n"
              "3.返回\n"
              "4.退出")
        print("讲师只能输入Alex,Jack")
        num = input("请选择:")
        if num == '1':
            if teachers_dict.get(name):
                teachers_dict[name].show_classroom(name)    #查看班级信息
            else:
                print("讲师只能输入Alex,Jack")
        elif num == '2':
            if teachers_dict.get(name):
                teachers_dict[name].show_student()        #查看学生信息
            else:
                print("讲师只能输入Alex,Jack")

        elif num == '3':
            break
        elif num == '4':
            sys.exit()
        else:
            continue


def school_view():      #学校视图
    flag = False
    while not flag:
        print("1.创建班级\n"
              "2.创建课程\n"
              "3.雇用讲师\n"
              "4.返回")
        num = input("请选择:")
        if num == '1':
            choice_school_obj.create_class()
        elif num == '2':
            choice_school_obj.create_course()
        elif num == '3':
            choice_school_obj.hire_teacher()
        elif num == '4':
            flag = True
        else:
            continue


def main():
    global dic
    global choice_school_obj
    dic = {}

    while True:
        print("欢迎进入选课系统".center(50,'*'))
        print("请选择学校:")
        choice_school = input("1.%s,2.%s,3.返回,4.退出"  % (s1.school_name,s2.school_name))
        if choice_school == '1':
            choice_school_obj = s1
        elif choice_school == '2':
            choice_school_obj = s2
        elif choice_school == '3':
            break
        elif choice_school_obj == '4':
            sys.exit(0)
        else:
            continue
        while True:
            print("1.学员视图\n"
                  "2.讲师视图\n"
                  "3.学校管理视图\n"
                  "4.返回\n"
                  "5.退出")
            num = input("请选择视图:")

            if num == '1':
                print("欢迎进入学生视图".center(50,'*'))
                students_view()
            elif num == '2':
                print("环境进入讲师视图".center(50,'*'))
                teacher_view()
            elif num == '3':
                print("欢迎进入学校管理视图".center(50,'*'))
                school_view()
            elif num == '4':
                break
            elif num == '5':
                sys.exit()
            else:
                continue

if __name__ == '__main__':
    classrooms = {}
    teachers_dict = {}
    courses_dict = {}
    stu_dict = {}
    s1 = School("老男孩_北京", "北京")
    s2 = School("老男孩_上海", "上海")
    course1 = Course("技术","Linux","38000","1 year","北京")
    course2 = Course("技术","Python","11000","7 month","北京")
    course3 = Course("技术","Go","7900","8 month","上海")
    courses_dict["Linux"] = course1
    courses_dict["Python"] = course2
    courses_dict["Go"] = course3
    t1 = Teacher("Alex","F","23","Python","S16","OldBoy_beijing")
    t2 = Teacher("Jack","F","28","Go","S19","OldBoy_shanghai")
    teachers_dict["Alex"] = t1
    teachers_dict["Jack"] = t2
    # teacher_dict = {"teacher_name":"Alex", "teacher_sex":"F","teacher_age":"23",
    #                 "teacher_course":"Python", "teacher_classroom":"S16", "teacher_school_name":"OldBoy_beijing"}
    # teacher_dict = {"teacher_name":"Jack", "teacher_sex":"F","teacher_age":"28",
    #                 "teacher_course":"Python", "teacher_classroom":"S16", "teacher_school_name":"OldBoy_shanghai"}
    print(s1,s2)
    main()
