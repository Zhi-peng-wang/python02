# 录入教师选课信息
def add_sel():
    print('*********添加教师选课信息**********')
    print('相关课程信息：\njava基础课程  5学分,  python基础课程  5学分，  数据库设计与应用  5学分\nJSP程序设计  6学分，  python高级应用  6学分，  jQuery开发基础教程  6学分')
    print('--'*50)
    print('******根据以上提供的课程信息，进行教师选课******')
    name = input('请输入教师姓名：')
    sel_course = input('请输入所选课程名称(请根据上面信息填写)：')
    sel_credit = input('请输入所选课程的学分数：')
    phone = input('请输入教师联系方式：')
    selection = [name, sel_course, sel_credit, phone]
    selection_list.append(selection)

# 查询教师选课信息
def query_sel(type):
    print('*************%s教师选课相关信息操作**************' % type)
    print('1.查询所有教师选课信息')
    print('2.输入教师姓名查询个人选课信息 ')
    num = int(input('选择操作：'))
    if num == 1:
        for x in range(0, len(selection_list)):
            selection = selection_list[x]
            name = selection[0]
            sel_course = selection[1]
            sel_credit = selection[2]
            phone = selection[3]
            print('序号：%s 教师姓名：%s 所选课程：%s 课程学分：%s 手机号：%s' % (x, name, sel_course, sel_credit, phone))
        return selection
    else:
        name = input('请输入教师姓名：')
        while 1:
            rs = False
            for selection in selection_list:
                if selection[0] == name:
                    index = selection_list.index(selection, 0, len(selection_list))
                    print('序号：%s 教师姓名：%s 所选课程：%s 课程学分：%s 手机号：%s' % (
                    index, selection_list[index][0], selection_list[index][1], selection_list[index][2],
                    selection_list[index][3]))
                    rs = True
            if rs == False:
                name = input('未找到相关教师信息，请重输：')
            else:
                break
        return selection

# 封装判断选择序号是否符合范围的函数
def select_num(type):
    index = input('请选择要%s的课程序号：' % type)
    index = int(index)
    while index not in range(0, len(selection_list)):
        index = input('选择的课程不存在，请重选：')
        index = int(index)
    # 返回选择的序号
    return index

# 修改选课信息
def alter_sel():
    if len(selection_list) == 0:
        print('没有相关课程信息，无法进行修改操作！')
        # 强制结束函数的执行，return下面的代码都不会再执行
        return
    query_sel('修改')
    index = int(select_num('修改'))
    selection = selection_list[index]
    new_name = input('请输入修改后的姓名（%s）：' % selection[0])
    new_sel_course = input('请输入修改后的选课名称（%s）:' % selection[1])
    new_sel_credit = input('请输入修改后的课程学分数（%s）:' % selection[2])
    new_phone = input('请输入修改后的手机号（%s）:' % selection[3])
    selection[0] = new_name
    selection[1] = new_sel_course
    selection[2] = new_sel_credit
    selection[3] = new_phone
    print('修改课程相关信息成功')

# 删除课程相关信息
def dele_sel():
    query_sel('删除')
    index = select_num('删除')
    rs = input('是否真的删除（y/n）:')
    if rs == 'y':
        selection_list.pop(index)
        print('删除成功')
    else:
        print('删除数据操作已取消！')


# 存储至本地文件
def save_data():
    file_handle = open('teacher_course_selecyion.txt', 'w')
    for selection in selection_list:
        # 把列表中的数据用空格分开拼接为一个字符串
        s = ' '.join(selection)
        file_handle.write(s)
        file_handle.write('\n')
    file_handle.close()

# 引入python内置函数os
import os

# 读取文件内容
def read_data():
    # 判断文件是否存在，如果存在，在做打开文件的操作
    # 如果文件存在返回true，否则返回False
    rs = os.path.exists('teacher_course_selecyion.txt')
    if rs == True:
        # 1，打开文件
        file_handle = open('teacher_course_selecyion.txt', mode='r')
        # 2.读取所有行
        contents = file_handle.readlines()
        # 3.取出每一个
        for msg in contents:
            # 去除\n
            msg = msg.strip('\n')
            # 使用 空格分割字符串
            selection = msg.split(' ')
            # 将小列表添加到大列表中
            selection_list.append(selection)
        file_handle.close()




selection_list = []
read_data()
def a():
    while 1:
        print('******************教师选课模块*******************')
        print('*****************1.录入教师选课信息*****************')
        print('*****************2.修改教师选课信息*****************')
        print('*****************3.查询教师选课信息*****************')
        print('*****************4.删除教师选课信息*****************')
        print('*******************0.退出程序*******************')
        num = input('请选择你的操作：')
        num = int(num)
        while num not in range(0, 5):
            num = int(input('您选择的选项不存在，请重选：'))
        if num == 1:
            # 录入教师选课信息
            add_sel()
            save_data()
        elif num == 2:
            # 修改教师选课信息
            alter_sel()
            save_data()
        elif num == 3:
            # 查询教师选课信息
            query_sel('查询')
        elif num == 4:
            # 删除教师选课信息
            print('1.通过序号删除课程信息')
            print('2.删除全部课程信息')
            num = input('请选择操作：')
            num = int(num)
            while num not in range(1, 4):
                num = int(input('所输选项不存在，请重输：'))
            if num == 1:
                dele_sel()
            elif num == 2:
                rs = input('是否真的删除（y/n）:')
                if rs == 'y':
                    selection_list.clear()
                    print('删除成功')
                else:
                    print('删除数据操作已取消！')

            save_data()
        else:
            print('退出程序')
            break
