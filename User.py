"""
# User.py
Configurations of User
包括class User定义 用户相关配置（登录验证、密码修改等）
Made by Hzj.
"""

class User(object):
    def __init__(self):
        self.Username = []
        self.Userpwd = []
        self.Adminname = "admin"
        self.Adminpwd = "password"

    def login(self):
        pass