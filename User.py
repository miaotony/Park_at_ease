"""
# User.py
Configurations of User
包括class User定义 用户相关配置（登录验证、密码修改等）
Made by Hzj.
"""

import time


class User(object):
    def __init__(self):
        self.Username = []
        self.Userpwd = []
        self.Adminname = "admin"
        self.Adminpwd = "password"

    def login(self):
        """
        用户登录
        :return:{bool}True(登录成功进入管理员模式)/False(登录失败返回用户模式)
        """
        cnt = 1  # counter for trial
        while 1 <= cnt <= 5:
            name = input('请输入用户名：')
            pwd = input('请输入密码：')
            if name == '' or pwd == '':
                print('用户名或密码不能为空！')
                continue
            elif name == self.Adminname and pwd == self.Adminpwd:
                return True
            else:
                if cnt <= 4:
                    print('用户名或密码错误，您还有%d次机会，请重试！' % (5-cnt))
                cnt += 1
        else:
            print('机会已用尽，即将返回用户界面......')
            time.sleep(2)
            return False
