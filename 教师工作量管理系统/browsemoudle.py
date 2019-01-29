# 添加教师的授课信息
def add_bro():
    print('*********添加教师个人授课信息**********')
    course_name = input('请输入课程名称：')
    teacher_name = input('请输入教授课程教师姓名：')
    class_name = input('请输入授课班级：')
    phone = input('请输入教师联系方式：')
    browse = [course_name, teacher_name, class_name, phone]
    browse_list.append(browse)

# 查询个人及所有教师的授课信息，以及根据课程查询相关老师的授课信息
def query_bro(type):
    print('*************%s教师授课信息操作**************' % type)
    print('1.查询所有教师授课信息')
    print('2.输入课程名称查询授课信息 ')
    num = int(input('选择操作：'))
    if num == 1:
        for x in range(0, len(browse_list)):
            browse = browse_list[x]
            course_name = browse[0]
            teacher_name = browse[1]
            class_name = browse[2]
            phone = browse[3]
            print('序号：%s 课程名称：%s 教师姓名：%s 授课班级：%s 手机号：%s' % (x, course_name, teacher_name, class_name, phone))
        return browse
    else:
        name = input('请输入课程名称：')
        while 1:
            rs = False
            for browse in browse_list:
                if browse[0] == name:
                    index = browse_list.index(browse, 0, len(browse_list))
                    print('序号：%s 课程名称：%s 教师姓名：%s 授课班级：%s 手机号：%s' % (
                    index, browse_list[index][0], browse_list[index][1], browse_list[index][2],
                    browse_list[index][3]))
                    rs = True
            if rs == False:
                name = input('未找到相关信息，请重输：')
            else:
                break
        return browse

# 存储至本地文件
def save_data():
    file_handle = open('teacher_browse.txt', 'w')
    for brose in browse_list:
        # 把列表中的数据用空格分开拼接为一个字符串
        s = ' '.join(brose)
        file_handle.write(s)
        file_handle.write('\n')
    file_handle.close()

# 引入python内置函数os
import os

# 读取文件内容
def read_data():
    # 判断文件是否存在，如果存在，在做打开文件的操作
    # 如果文件存在返回true，否则返回False
    rs = os.path.exists('teacher_browse.txt')
    if rs == True:
        # 1，打开文件
        file_handle = open('teacher_browse.txt', mode='r')
        # 2.读取所有行
        contents = file_handle.readlines()
        # 3.取出每一个
        for msg in contents:
            # 去除\n
            msg = msg.strip('\n')
            # 使用 空格分割字符串
            browse = msg.split(' ')
            # 将小列表添加到大列表中
            browse_list.append(browse)
        file_handle.close()

# 声明一个大列表
browse_list = []
read_data()
def a():
    while 1:
        print('****************教师信息浏览模块*****************')
        print('*****************1.添加教师个人授课信息*****************')
        print('*****************2.查询教师授课信息*****************')
        print('*******************0.退出程序*******************')
        num = input('请选择你的操作：')
        num = int(num)
        while num not in range(0, 5):
            num = int(input('您选择的选项不存在，请重选：'))
        if num == 1:
            # 添加教师个人授课信息
            add_bro()
            save_data()
        elif num == 2:
            # 查询教师授课信息
            query_bro('查询')
        else:
            print('退出程序')
            break
