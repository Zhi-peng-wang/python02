# 录入相关信息
def add_sta():
    print('*********添加工作量信息**********')
    name = input('请输入教师姓名：')
    course = input('请输入教师所教授课程：')
    stu_num = int(input('请输入教师教授课程的班级人数(只输入数字)：'))

    if stu_num < 40:
        print("人头系数为：0.9")
    elif stu_num > 50:
        print("人头系数为：1.1")
    else:
        print("人头系数为：1.0")

def a():
    while 1:
        print('*************************教师工作量统计模块*********************')
        print('*****************1.录入相关信息并计算教师工作量*****************')
        print('****************************0.退出程序**************************')
        num = input('请选择你的操作：')
        num = int(num)
        while num not in range(0, 2):
            num = int(input('您选择的选项不存在，请重选：'))
        if num == 1:
            # 添加教师信息
            add_sta()
        else:
            print('退出程序')
            break