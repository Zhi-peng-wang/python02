import teacherinfo
import browsemoudle
import course_infomation
import teacher_course_selection
import statistics

def login():# 登陆
    def showMessage():
        print('---新建用户：（键入N/n）---')
        print('---登录帐号：（键入E/e）---')
        print('---退出程序：（键入Q/q）---')

    def new_user():
        while True:
            myname = input("请输入用户名：")
            if myname in user:
                print('你输入的用户名已存在，重新输入。')
                continue
            else:
                user[myname] = input('请输入密码：')
                print('注册成功，赶紧登录试试吧！')
                break

    def older_user():
        while True:
            in_name = input('请输入登录用户名：')
            if in_name in user:
                in_password = input('请输入登录密码：')
                if in_password == user[in_name]:
                    print('******登录成功！******\n')
                    m = input("需要更改密码吗？(y/n)请输入")
                    if m == 'y':
                        modify()
                    elif m == 'n':
                        print('---' * 30)
                        # 登陆成功后，操作
                        operation()
                    else:
                        print("您输入有误，默认您不修改密码，若要修改请退出程序，重新登陆修改面膜")
                    break
                else:
                    print('你输入的密码有误！\n')
                    break
            else:
                print('你输入的用户名不存在')
                continue
    def modify():
        print('******更改密码******')
        username = input("请输入您的用户名称：")
        print('您的初始密码：'+ user[username])
        cpassword = input('请输入您的新密码：')
        rcpassword = input('请确认您的新密码：')
        if cpassword == rcpassword :
            user[username] = rcpassword
            print('更改后的相关信息如下：')
            print('您的新密码：'+user[username])
            print('---' * 30)
            # 登陆成功后，操作
            operation()
        else:
            print('俩次密码不一致，请重新设定！')
            modify()
    def operation():
        while 1:
            print('*******************教师工作量管理系统********************')
            print('******************1.教师个人信息管理模块*****************')
            print('******************2.教师信息浏览模块*****************')
            print('******************3.教师课程信息模块*****************')
            print('******************4.教师选课模块*****************')
            print('******************5.统计模块*****************')
            print('*******************0.退出程序*******************')
            num = input('请选择你的操作：')
            num = int(num)
            while num not in range(0, 6):
                num = int(input('您选择的选项不存在，请重选：'))
            if num == 1:
                # 教师个人信息管理模块
                teacherinfo.a()
            elif num == 2:
                # 教师信息浏览模块
                browsemoudle.a()
            elif num == 3:
                # 教师课程信息模块
                course_infomation.a()
            elif num == 4:
                # 教师选课模块
                teacher_course_selection.a()
            elif num == 5:
                # 统计模块
                statistics.a()
            else:
                print('感谢您的使用\n退出程序')
                break
    user = {'admin':'123',}
    while True:
        showMessage()
        myIn = input('---请输入指令代码：')
        if myIn in 'nN':
            new_user()
        elif myIn in 'eE':
            older_user()
            break
        elif myIn in 'mM':
            modify()
            break
        elif myIn in 'Qq':
            print('感谢您的使用\n程序已退出')
            break
        else:
            print('你输入的指令有误，重新输入。')
            continue

if __name__ == '__main__':
    login()