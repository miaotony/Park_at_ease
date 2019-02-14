"""
# Car.py
Configurations of Car.
包括class Car&ParkManage定义、车辆管理（新增、删除、修改等）
Made by Hzj.
"""

from enum import Enum, unique
import time

Model = Enum('Model', ("小汽车", "小卡", "中卡", "大卡"))
Color = Enum('Color', ("白色", "黑色", "灰色", "蓝色", "红色", "黄色"))


class ParkManage(object):
    def __init__(self, max_car=150):
        self.max_car = max_car
        self.carlist = []
        self.carnum = len(self.carlist)


    def check_car(self, car):
        """确定是否已存在当前车辆，若存在则返回当前车辆信息"""
        for parkedCar in self.carlist:
            if parkedCar.carnum == car.carnum:
                return parkedCar
        else:
            return None


    def park(self):
        """输入车辆信息，停车"""
        if self.carnum >= self.max_car:
            print("对不起，当前车库已满！")
            return None
        temp_parknum = input('请输入所停车位:')
        temp_carnum = input('请输入车牌号:')
        temp_model = int(input('请输入车型序号（1小汽车, 2小卡, 3中卡, 4大卡）:'))
        temp_color = input('请输入车辆颜色序号（1白色, 2黑色, 3灰色, 4蓝色, 5红色, 6黄色）:')

        temp_car = Car(temp_parknum, temp_carnum, temp_model, temp_color)
        self.add_car(temp_car)


    def add_car(self, car):
        """从car新增车辆到carlist中"""
        if self.check_car(car) is not None:
            print("车辆已存在，请重试！")
        else:
            car["intime"] = time.ctime()  # 调用当前时间?
            self.carlist.append(car)
            print("%s 停车入库成功！" % car.carnum)


    def display(self):
        for parkedcar in self.carlist:
            print(parkedcar)





class Car(ParkManage):
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
        return "%4s %5s %5s %6s %s" % \
            (self.parknum, self.carnum, self.model, self.color, self.intime)



    
             
        
        
