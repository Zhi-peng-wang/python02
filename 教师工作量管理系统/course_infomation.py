# 课程信息录入
def add_cou():
    print('*********添加此门课程相关信息**********')
    course_name = input('请输入课程名称：')
    number = input('请输入上课班级人数：')
    num_banji = input('请输入班级个数：')
    credit = input('请输入此门课程的学分数：')
    class_num = input('请输入此门课程的课时数：')
    course = [course_name, number, num_banji, credit, class_num]
    course_list.append(course)

# 查询课程信息
def query_cou(type):
    print('*************%s课程相关信息操作**************' % type)
    print('1.查询所有课程信息')
    print('2.输入课程名称查询 ')
    num = int(input('选择操作：'))
    if num == 1:
        for x in range(0, len(course_list)):
            course = course_list[x]
            course_name = course[0]
            number = course[1]
            num_banji = course[2]
            credit = course[3]
            class_num = course[4]
            print('序号：%s 课程名称：%s 班级人数：%s 上课班级数：%s 学分数：%s 课时数：%s' % (x, course_name, number, num_banji, credit, class_num))
        return course
    else:
        name = input('请输入课程名称：')
        while 1:
            rs = False
            for course in course_list:
                if course[0] == name:
                    index = course_list.index(course, 0, len(course_list))
                    print('序号：%s 课程名称：%s 班级人数：%s 上课班级数：%s 学分数：%s 课时数：%s' % (
                    index, course_list[index][0], course_list[index][1], course_list[index][2],
                    course_list[index][3], course_list[index][4]))
                    rs = True
            if rs == False:
                name = input('未找到相关教师信息，请重输：')
            else:
                break
        return course

# 封装判断选择序号是否符合范围的函数
def select_num(type):
    index = input('请选择要%s的课程序号：' % type)
    index = int(index)
    while index not in range(0, len(course_list)):
        index = input('选择的课程不存在，请重选：')
        index = int(index)
    # 返回选择的序号
    return index

def alter_cou():
    if len(course_list) == 0:
        print('没有课程相关信息，无法进行修改操作！')
        # 强制结束函数的执行，return下面的代码都不会再执行
        return
    query_cou('修改')
    index = int(select_num('修改'))
    course = course_list[index]
    new_course_name = input('请输入修改后的课程名称（%s）：' % course[0])
    new_number = input('请输入修改后的班级人数（%s）:' % course[1])
    new_num_banji = input('请输入修改后的上课班级数（%s）:' % course[2])
    new_credit= input('请输入修改后的课程的学分数（%s）:' % course[3])
    new_class_num = input('请输入修改后的课程的学分数（%s）:' % course[4])
    course[0] = new_course_name
    course[1] = new_number
    course[2] = new_num_banji
    course[3] = new_credit
    course[4] = new_class_num
    print('修改教师相关信息成功')

# 删除课程信息
def dele_cou():
    query_cou('删除')
    index = select_num('删除')
    rs = input('是否真的删除（y/n）:')
    if rs == 'y':
        course_list.pop(index)
        print('删除成功')
    else:
        print('删除数据操作已取消！')

# 存储至本地文件
def save_data():
    file_handle = open('course_infomation.txt', 'w')
    for course in course_list:
        # 把列表中的数据用空格分开拼接为一个字符串
        s = ' '.join(course)
        file_handle.write(s)
        file_handle.write('\n')
    file_handle.close()

# 引入python内置函数os
import os

# 读取文件内容
def read_data():
    # 判断文件是否存在，如果存在，在做打开文件的操作
    # 如果文件存在返回true，否则返回False
    rs = os.path.exists('course_infomation.txt')
    if rs == True:
        # 1，打开文件
        file_handle = open('course_infomation.txt', mode='r')
        # 2.读取所有行
        contents = file_handle.readlines()
        # 3.取出每一个
        for msg in contents:
            # 去除\n
            msg = msg.strip('\n')
            # 使用 空格分割字符串
            course = msg.split(' ')
            # 将小列表添加到大列表中
            course_list.append(course)
        file_handle.close()

# 声明一个大列表
course_list = []
read_data()
def a():
    while 1:
        print('****************课程信息浏览管理模块*****************')
        print('*****************1.添加课程信息*****************')
        print('*****************2.修改课程信息*****************')
        print('*****************3.查询课程信息*****************')
        print('*****************4.删除课程信息*****************')
        print('*******************0.退出程序*******************')
        num = input('请选择你的操作：')
        num = int(num)
        while num not in range(0, 5):
            num = int(input('您选择的选项不存在，请重选：'))
        if num == 1:
            # 添加课程信息
            add_cou()
            save_data()
        elif num == 2:
            # 修改课程信息
            alter_cou()
            save_data()
        elif num == 3:
            # 查询课程信息
            query_cou('查询')
        elif num == 4:
            # 删除课程信息
            print('1.通过序号删除课程信息')
            print('2.删除全部课程信息')
            print('3.根据课程名称删除')
            num = input('请选择操作：')
            num = int(num)
            while num not in range(1, 4):
                num = int(input('所输选项不存在，请重输：'))
            if num == 1:
                dele_cou()
            elif num == 2:
                rs = input('是否真的删除（y/n）:')
                if rs == 'y':
                    course_list.clear()
                    print('删除成功')
                else:
                    print('删除数据操作已取消！')
            else:
                name = input('请输入想要删除课程的名称：')
                rs = input('是否真的删除（y/n）:')
                if rs == 'y':
                    while 1:
                        rs = False
                        for course in course_list:
                            if course[0] == name:
                                course_list.remove(course)
                                print(course_list)
                                print('删除成功')
                                rs = True
                        if rs == False:
                            # print('未找到请重新输入')
                            name = input('未找到相关课程，请重输：')
                        else:
                            break
                else:
                    print('删除数据操作已取消！')
            save_data()
        else:
            print('退出程序')
            break