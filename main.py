# -*- coding: utf-8 -*-
"""
CEIESTA_Advanced Guide for Winter Vacation
Section2 Course Design
四院科协寒假进阶指南Section2小课设
基于Python实现 by Hzj~
Miao~
@DevelopTime:2019.2.6, 2.14-
@Version:V0.3.0
@UpdateTime:2019.2.18晚

# main.py
"""


import os
import logging
import re   # 正则表达式
import time

# Sub module
from Car import Car, ParkManage, Model, Color
from User import User
# from GUI import *  # developing
# from IO import *  # developing


def menu_select(isAdmin, park):
    """显示菜单，返回str型操作码"""
    if isAdmin == True:
        # 管理员模式
        while True:
            os.system("cls")
            print("""
            ***欢迎使用停车场管理系统***
                  ## 管理员模式 ##    
                  
            ---北京第三区交通委提醒您---
           |   道路千万条，安全第一条   |
           |   行车不规范，亲人两行泪   |
            ---------------------------
      本停车场总车位数：%3d  当前空闲车位数：%3d 
    
                1)停车
                2)取车
                3)显示车辆信息
                4)查询车辆信息
                5)编辑车辆信息
                6)统计车辆信息
                7)从文件加载车辆
                
                8)切换至用户模式
                9)关于
                0)退出系统    
            """ % (park.max_car, park.max_car-len(park.carlist)))
            c = input("请输入操作码(0~9):")
            if re.match(r'(^\d$)', c):
                if 0 <= int(c) <= 9:    # c >= 0 and c <= 9
                    return c
                else:
                    print("输入错误，请重试！")
            else:
                print("输入错误，请重试！")
            '''
            try:
                c = int(input("请输入操作码(0~8):"))
            except Exception as e:
                logging.exception(e)
                c = -1
                continue
            '''


    elif isAdmin == False:
        # 用户模式
        while True:
            os.system("cls")
            print("""
            ***欢迎使用停车场管理系统***
                   ## 用户模式 ##   
                   
            ---北京第三区交通委提醒您---
           |   道路千万条，安全第一条   |
           |   行车不规范，亲人两行泪   |
            ---------------------------
      本停车场总车位数：%3d  当前空闲车位数：%3d 
    
                1)停车
                2)取车
                3)查询车辆信息
                
                4)切换至管理员模式
                5)关于
                0)退出系统    
            """ % (park.max_car, park.max_car-len(park.carlist)))
            c = input("请输入操作码(0~5):")
            if re.match(r'(^\d$)', c):
                if 0 <= int(c) <= 5:    # c >= 0 and c <= 5
                    return c
                else:
                    print("输入错误，请重试！")
            else:
                print("输入错误，请重试！")

            '''
            try:
                c = int(input("请输入操作码(0~5):"))
            except Exception as e:
                print('请输入正确的操作码！')
                logging.exception(e)
                c = -1
                continue
            '''


def main():
    park = ParkManage()  # 建立并初始化车库
    user = User()  # 初始化用户
    user.login()
    isAdmin = True  # 测试用

    while True:
        choice = menu_select(isAdmin, park=park)
        if not isAdmin:
            # 用户
            if choice == '0':
                os.system("cls")  # 清屏
                print("Goodbye.\nHave a nice day!\n期待与您下一次的相遇！ \n\n系统3秒后自动关闭...")
                time.sleep(3)
                exit(0)
            elif choice == '1':  # 停车
                os.system("cls")  # 清屏
                park.park(isAdmin)
            elif choice == '2':  # 取车
                park.pickup()
                os.system("pause")
            elif choice == '3':  # 查车
                os.system("cls")
                park.inquire()
                os.system("pause")
            elif choice == '4':  # 切换到管理员模式
                isAdmin = True
                continue
            elif choice == '5':  # 关于
                os.system("cls")  # 清屏
                print("""
                      停车场管理系统
                       Version:0.3.0
                    Copyright by Hzj.
                   All rights reserved.

                 """)
                os.system("pause")
            else:
                pass

        elif isAdmin:
            # 管理员
            if choice == '0':  # 退出
                os.system("cls")  # 清屏
                print("Goodbye.\nHave a nice day!\n期待与您下一次的相遇！ \n\n系统3秒后自动关闭...")
                time.sleep(3)
                exit(0)
            elif choice == '1':  # 停车
                os.system("cls")  # 清屏
                park.park(isAdmin)
            elif choice == '2':  # 取车
                os.system("cls")  # 清屏
                park.pickup()
                os.system("pause")
            elif choice == '3':  # 显示车辆信息
                os.system("cls")  # 清屏
                park.display()
                os.system("pause")
            elif choice == '4':  # 查询车辆信息
                os.system("cls")
                park.inquire()
                os.system("pause")
            elif choice == '5':  # 编辑车辆信息
                os.system("cls")  # 清屏
                pass
            elif choice == '6':  # 统计车辆信息
                os.system("cls")  # 清屏
                pass
            elif choice == '7':  # 从文件加载车辆
                os.system("cls")  # 清屏
                pass
            elif choice == '8':  # 切换到用户模式
                isAdmin = False
            elif choice == '9':  # 关于
                os.system("cls")  # 清屏
                print("""
                      停车场管理系统
                       Version:0.3.0
                    Copyright by Hzj.
                   All rights reserved.

                     """)
                os.system("pause")
            else:
                pass


if __name__ == '__main__':
    main()
