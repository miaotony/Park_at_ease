"""
# Car.py
Configurations of Car.
包括class Car&ParkManage定义、车辆管理（新增、删除、修改等）
Made by Hzj.
"""

from enum import Enum, unique
import time
import re
import os
import logging

Model = Enum('Model', ("小汽车", "小卡", "中卡", "大卡"))
Color = Enum('Color', ("白色", "黑色", "灰色", "蓝色", "红色", "黄色"))

class Car(object):  # ParkManage
    def __init__(self, parknum, carnum, model, color):
        # super(Car, self).__init__()
        self.parknum = parknum
        self.carnum = carnum
        self.model = model
        self.color = color
        self.intime = None

        """
        car.carnum = None
        car.intime = None
        """

    def __setitem__(self, key, value):
        self.__dict__[key] = value
    def __getitem__(self, key):
        return self.__dict__[key]

    def __str__(self):
        """
        # car_model judgment: enum：num->中文
        if self.model == '0':
            self.model = "小汽车"
        elif self.model == '1':
            self.model = "小卡"
        elif self.model == '2':
            self.model = "中卡"
        elif self.model == '3':
            self.model = "大卡"

        # car_color judgment: enum：num->中文
        if self.color == '0':
            self.color = "黑色"
        elif self.color == '1':
            self.color = "白色"
        elif self.color == '2':
            self.color = "灰色"
        elif self.color == '3':
            self.color = "蓝色"
        elif self.color == '4':
            self.color = "红色"
        elif self.color == '5':
            self.color = "黄色"
        """
        return "%4s   %8s %6s %4s   %s" % \
            (self.parknum, self.carnum, self.model.name, self.color.name, self.intime)



class ParkManage(object):
    def __init__(self, max_car=150):
        self.max_car = max_car
        self.carlist = []
        self.carnum = len(self.carlist)

    def check_empty(self, model=1):
        """
        查询空闲车位，model=1默认按小汽车查询
        :return:[list]空闲车位号列表
        """
        if model == 1:
            # t_num = [parkedcar["parknum"] for parkedcar in self.carlist]
            """
            t_list = []
            for i in range(self.max_car):
                if i not in t_num:
                    t_list.append(i)
            return t_list
            """
            # return [i for i in range(self.max_car) if i not in t_num]
            return [i for i in range(self.max_car) if i not in
                    [parkedcar["parknum"] for parkedcar in self.carlist]]




    def check_car(self, car, sort='1'):
        """
        用于查找车辆。默认sort='1',按照车位查找，若存在则返回占用车辆信息。
        :return:[class]Car
        """
        for parkedCar in self.carlist:
            if sort == '1' and parkedCar.parknum == car.parknum:  # 车位
                return parkedCar
            elif sort == '2' and parkedCar.carnum == car.carnum:  # 车牌
                return parkedCar
        return None

    def check_car_num(self, carnum):
        """
        基于正则表达式判断车牌号是否合法，合法为True
        :return:[bool]True/False
        """
        #### Unfinished!!!!!!!!!!!!!!!!!
        return True

    def park(self, isAdmin):
        """
        输入车辆信息，停车。管理员isAdmin==1时询问是否继续停车。
        :return:None
        """
        if self.carnum >= self.max_car:
            print("对不起，当前车库已满！")
            return None
        while True:
            print('当前空闲车位如下：')
            print(self.check_empty())
            ## 变量初始化
            flag_right_input = False
            flag_error = 0  # 清除错误flag
            temp_parknum = None
            temp_carnum = None
            temp_color = None
            temp_model = None
            try:
                temp_parknum = int(input('请输入所停车位:'))
                temp_carnum = input('请输入车牌号:')
                temp_model = int(input('请输入车型序号（1小汽车, 2小卡, 3中卡, 4大卡）:'))
                temp_color = int(input('请输入车辆颜色序号（1白色, 2黑色, 3灰色, 4蓝色, 5红色, 6黄色）:'))

                ## 以下为输入信息是否有效的判断
                if 0 <= temp_parknum <= self.max_car:  # 判断车位是否在合理范围内
                    if 1 <= temp_model <= 4:
                        temp_model = Model(temp_model)  # 转化为Model枚举类型
                        if 1 <= temp_color <= 6:
                            temp_color = Color(temp_color)  # 转化Color枚举类型
                            if self.check_car_num(temp_carnum):  # 判断车牌号是否有效
                                for parkedCar in self.carlist:
                                    if parkedCar.parknum == temp_parknum:  # 判断车位是否已被占用
                                        flag_error = 1
                                        break
                                    elif parkedCar.carnum == temp_carnum:  # 判断车牌是否已重复
                                        flag_error = 2
                                        break
                                else:
                                     flag_right_input = True  # 以上判断均通过
                            """
                            else:
                                error_input = 3
                        else:
                            error_input = 4
                    else:
                        error_input = 5
                    """

            except Exception as e:
                logging.exception(e)  # for test
                flag_right_input = False
                # error_input = 6  # 输入类型错误
            finally:
                # if error_input != 0:
                if not flag_right_input:
                    if flag_error == 1:
                        print('当前车位已被占用！')
                    elif flag_error == 2:
                        print('车牌号重复！')
                    else:
                        print("输入错误！")
                    retry_choice = input('按<F>键返回主菜单，按其他任意键重试')
                    if retry_choice == 'F' or retry_choice == 'f':
                        return None  # 返回主菜单
                    else:
                        os.system('cls')  # 清屏
                else:
                    # 通过各项判断，下面新增车辆
                    temp_car = Car(temp_parknum, temp_carnum, temp_model, temp_color)
                    temp_car["intime"] = time.ctime()  # 调用当前时间
                    self.carlist.append(temp_car)
                    print("%s 停车入库成功！" % temp_carnum)
                    if not isAdmin:
                        input('按任意键返回主菜单......')
                        return None  # 用户返回主菜单

                    if isAdmin:  # 管理员询问是否继续新增车辆
                        while True:
                            continue_choice = input("是（Y）否（N）继续新增车辆？")
                            if continue_choice == 'Y' or continue_choice == 'y':
                                os.system('cls')  # 清屏
                                break
                            elif continue_choice == 'N' or continue_choice == 'n':
                                return None
                            else:
                                print('输入错误，请重试！')

    """
    def add_car(self, car):
        # 从car新增车辆到carlist中
        # if self.check_car(car) is not None:
        #     print("车辆已存在，请重试！")
        # else:
        car["intime"] = time.ctime()  # 调用当前时间
        self.carlist.append(car)
        print("%s 停车入库成功！" % car.carnum)
    """

    def display(self):
        """
        显示车辆信息
        :return:None
        """
        print("车位   车牌号       车型    颜色    入场时间 ")
        i = 0
        for parkedcar in self.carlist:
            print(parkedcar)
            i += 1
            if i % 10 == 0:  # 每10辆一页
                print("按任意键查看下一页......")
                os.system("pause")
                print("车位   车牌号       车型    颜色    入场时间 ")

    def pickup(self):
        """
        取车
        :return:
        """
        pass









    
             
        
        
