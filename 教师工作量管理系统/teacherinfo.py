'''
分析：
① 个人信息录入 （主要包括个人授课信息）
② 个人信息删除
1. 录入相关教师信息 使用大列表嵌套小列表，小列表存储一个教师的全部信息
    再将其存入txt文件中
2. 查询是一个公共的，根据需要删除时也需要查询操作。所以定义一个带参数查询函数，以共下面删除函数
    使用
3. 根据序号查询时，
4. 修改和删除函数，根据返回值，来判定修改的序号(第三步的作用)
5. 将录入信息存入文件中
6. 导入python内置函数os，用来规范录入读取文件等操作
7. 最后进行相关操作的选择
'''

# 添加
def add_tea():
    print('*********添加教师个人信息**********')
    name = input('请输入教师姓名：')
    banji = input('请输入教师的所教班级：')
    course = input('请输入教师所教授课程：')
    phone = input('请输入教师联系方式：')
    teacher = [name, banji, course, phone]
    teacher_list.append(teacher)

# 查询
def query_tea(type):
    print('*************%s教师相关信息操作**************' % type)
    print('1.查询所有教师信息')
    print('2.输入教师姓名查询 ')
    num = int(input('选择操作：'))
    if num == 1:
        for x in range(0, len(teacher_list)):
            teacher = teacher_list[x]
            name = teacher[0]
            banji = teacher[1]
            course = teacher[2]
            phone = teacher[3]
            print('序号：%s 姓名：%s 教授班级：%s 教授课程：%s 手机号：%s' % (x, name, banji, course, phone))
        return teacher
    else:
        name = input('请输入教师姓名：')
        while 1:
            rs = False
            for teacher in teacher_list:
                if teacher[0] == name:
                    index = teacher_list.index(teacher, 0, len(teacher_list))
                    print('序号：%s 姓名：%s 教授班级：%s 教授课程：%s 手机号：%s' % (
                    index, teacher_list[index][0], teacher_list[index][1], teacher_list[index][2],
                    teacher_list[index][3]))
                    rs = True
            if rs == False:
                name = input('未找到相关教师信息，请重输：')
            else:
                break
        return teacher

# 封装判断选择序号是否符合范围的函数
def select_num(type):
    index = input('请选择要%s的教师序号：' % type)
    index = int(index)
    while index not in range(0, len(teacher_list)):
        index = input('选择的教师不存在，请重选：')
        index = int(index)
    # 返回选择的序号
    return index

# 修改
def alter_tea():
    if len(teacher_list) == 0:
        print('没有教师相关信息，无法进行修改操作！')
        # 强制结束函数的执行，return下面的代码都不会再执行
        return
    query_tea('修改')
    index = int(select_num('修改'))
    teacher = teacher_list[index]
    new_name = input('请输入修改后的姓名（%s）：' % teacher[0])
    new_banji = input('请输入修改后的教授班级（%s）:' % teacher[1])
    new_course = input('请输入修改后的教授课程（%s）:' % teacher[2])
    new_phone = input('请输入修改后的手机号（%s）:' % teacher[3])
    teacher[0] = new_name
    teacher[1] = new_banji
    teacher[2] = new_course
    teacher[3] = new_phone
    print('修改教师相关信息成功')

# 删除
def dele_tea():
    query_tea('删除')
    index = select_num('删除')
    rs = input('是否真的删除（y/n）:')
    if rs == 'y':
        teacher_list.pop(index)
        print('删除成功')
    else:
        print('删除数据操作已取消！')

# 存储至本地文件
def save_data():
    file_handle = open('teacher_infomation.txt', 'w')
    for teacher in teacher_list:
        # 把列表中的数据用空格分开拼接为一个字符串
        s = ' '.join(teacher)
        file_handle.write(s)
        file_handle.write('\n')
    file_handle.close()

# 引入python内置函数os
import os

# 读取文件内容
def read_data():
    # 判断文件是否存在，如果存在，在做打开文件的操作
    # 如果文件存在返回true，否则返回False
    rs = os.path.exists('teacher_infomation.txt')
    if rs == True:
        # 1，打开文件
        file_handle = open('teacher_infomation.txt', mode='r')
        # 2.读取所有行
        contents = file_handle.readlines()
        # 3.取出每一个
        for msg in contents:
            # 去除\n
            msg = msg.strip('\n')
            # 使用 空格分割字符串
            teacher = msg.split(' ')
            # 将小列表添加到大列表中
            teacher_list.append(teacher)
        file_handle.close()



# 声明一个大列表
teacher_list = []
read_data()
def a():
    while 1:
        print('****************教师信息管理系统*****************')
        print('*****************1.添加教师信息*****************')
        print('*****************2.修改教师信息*****************')
        print('*****************3.查询教师信息*****************')
        print('*****************4.删除教师信息*****************')
        print('*******************0.退出程序*******************')
        num = input('请选择你的操作：')
        num = int(num)
        while num not in range(0, 5):
            num = int(input('您选择的选项不存在，请重选：'))
        if num == 1:
            # 添加教师信息
            add_tea()
            save_data()
        elif num == 2:
            # 修改教师信息
            alter_tea()
            save_data()
        elif num == 3:
            # 查询教师信息
            query_tea('查询')
        elif num == 4:
            # 删除教师信息
            print('1.通过序号删除教师信息')
            print('2.删除全部教师信息')
            print('3.根据教师姓名删除')
            num = input('请选择操作：')
            num = int(num)
            while num not in range(1, 4):
                num = int(input('所输选项不存在，请重输：'))
            if num == 1:
                dele_tea()
            elif num == 2:
                rs = input('是否真的删除（y/n）:')
                if rs == 'y':
                    teacher_list.clear()
                    print('删除成功')
                else:
                    print('删除数据操作已取消！')
            else:
                name = input('请输入想要删除教师的姓名：')
                rs = input('是否真的删除（y/n）:')
                if rs == 'y':
                    while 1:
                        rs = False
                        for teacher in teacher_list:
                            if teacher[0] == name:
                                teacher_list.remove(teacher)
                                print(teacher_list)
                                print('删除成功')
                                rs = True
                        if rs == False:
                            # print('未找到请重新输入')
                            name = input('未找到相关教师，请重输：')
                        else:
                            break
                else:
                    print('删除数据操作已取消！')
            save_data()
        else:
            print('退出程序')
            break