# -*- coding: utf-8 -*-
"""
# Car.py
Configurations of Car.
包括class Car&ParkManage定义、车辆管理（新增、删除、修改等）
Made by Hzj.
"""

from enum import Enum
import time
import re
import os
import logging

Model = Enum('Model', ("小汽车", "小卡", "中卡", "大卡"))
Color = Enum('Color', ("白色", "黑色", "灰色", "蓝色", "红色", "黄色"))
unit_price = 5  # 每小时单价为5元


class Car(object):  # ParkManage
    def __init__(self, parknum, carnum, model, color, intime=None):
        # super(Car, self).__init__()
        self.parknum = parknum
        self.carnum = carnum
        self.model = model
        self.color = color
        self.intime = intime

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getitem__(self, key):
        return self.__dict__[key]

    def __str__(self):
        return "%4s   %-8s   %-6s   %-s   %s" % \
            (self.parknum, self.carnum, self.model.name, self.color.name, self.intime)


class ParkManage(object):
    def __init__(self, max_car=150):
        self.max_car = max_car
        self.carlist = []
        # self.carnum = len(self.carlist)

    def check_empty(self, model=1):
        """
        查找空闲车位，model=1默认按小汽车查找
        :return:{list}空闲车位号列表
        """
        if model == 1:
            # t_num = [parkedCar["parknum"] for parkedCar in self.carlist]
            """
            t_list = []
            for i in range(self.max_car):
                if i not in t_num:
                    t_list.append(i)
            return t_list
            """
            # return [i for i in range(self.max_car) if i not in t_num]
            return [i for i in range(self.max_car) if i not in
                    [parkedCar["parknum"] for parkedCar in self.carlist]]

    def inquire_empty(self):
        """
        查询空闲车位，调用即可进行输出。
        :return: None
        """
        t_i = 0
        for t_empty in self.check_empty():
            print("%3s  " % t_empty, end='')
            t_i += 1
            if len(self.check_empty()) > 15 and t_i % 15 == 0:  # 每15个一行
                print('')

    def check_car_num(self, carnum):
        """
        基于正则表达式判断车牌号是否合法，合法为True
        :return:{bool}True/False
        """
        # return True  # TODO DEBUG
        car_license = re.compile(u"^[\u4e00-\u9fa5][A-Z][A-Z0-9]{5}$")  # e.g.: 苏BCD123
        if car_license.match(carnum):
            return True
        else:
            return False

    def park(self, isAdmin):
        """
        输入车辆信息，停车。管理员isAdmin==1时询问是否继续停车。
        :return:None
        """
        if len(self.carlist) >= self.max_car:
            print("对不起，当前车库已满！")
            return None
        while True:
            print('当前空闲车位如下：')
            self.inquire_empty()
            print('')

            # 变量初始化
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

                # 以下为输入信息是否有效的判断
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
                # logging.exception(e)  # for debug
                flag_right_input = False  # 输入类型错误
                # error_input = 6
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

                    if not isAdmin:  # 用户返回主菜单
                        print('按任意键返回主菜单......')
                        os.system("pause")
                        return None
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

    def display(self, carlist=None):
        """
        显示车辆信息
        :param:{list}carlist, 默认为self.carlist
        :return:None
        """
        if carlist is None:
            carlist = self.carlist
            if len(self.carlist) == 0:
                print("停车场内暂无车辆。")
                return None

        print("车位    车牌号     车型       颜色    入场时间 ")
        i = 0
        for parkedCar in carlist:
            print(parkedCar)
            i += 1
            if len(carlist) > 10 and i % 10 == 0:  # 超过10辆车则每10辆一页
                print("按任意键查看下一页......")
                os.system("pause")
                print("车位    车牌号     车型       颜色    入场时间 ")
        # os.system('pause')

    def check_car(self, keyword, sort=1):
        """
        用于查找车辆。默认sort=1,按照车位查找，若存在则返回满足条件的车辆信息。
        :param:keyword关键词，sort查找方式
        :return:{class Car}/{list}
        """
        if sort == 1:  # 按车位
            for parkedCar in self.carlist:
                if parkedCar.parknum == keyword:
                    return parkedCar
        elif sort == 2:  # 按车牌
            for parkedCar in self.carlist:
                if parkedCar.carnum == keyword:
                    return parkedCar
        elif 3 <= sort <= 4:
            if sort == 3:  # 按车型
                key = "model"
            elif sort == 4:  # 按颜色
                key = "color"
            else:
                return None
            t_list = []
            for parkedCar in self.carlist:
                if parkedCar[key] == keyword:
                    t_list.append(parkedCar)
            return t_list
        elif sort == 5:  # TODO 按入场时间
            #  (developing)
            pass
        else:
            return None

    def inquire(self, choice=-1):
        """
        查询信息
        复用于取车的查找，修改信息的查找。
        Developing:按照入场时间查询（多少时间内）。
        :param choice:查询方式选择，默认为-1.
        :return:None/{class Car}parkedCar
        """
        # choice = -1  # DEBUG
        while choice < 0 or choice > 6:
            print("""
                1)空闲车位查询
                --车辆信息查询--
                2)按车位查询车辆
                3)按车牌查询车辆
                4)按车型查询车辆
                5)按颜色查询车辆
                6)按入场时间查询(developing)
                ---------------------------
                0)返回主菜单
            """)
            try:
                choice = int(input("请输入操作码："))
            except Exception:
                print("错误操作码，请重试！")
                continue
            if choice < 0 or choice > 6:
                print("错误操作码，请重试！")

        if choice == 0:
            return None  # 返回主菜单
        # 空闲车位查询：
        elif choice == 1:
            if len(self.carlist) >= self.max_car:
                print("对不起，当前车库已满！")
                return None
            else:
                print('空闲车位如下：')
                self.inquire_empty()
                print('')  # 多空一行
        else:
            if len(self.carlist) == 0:
                print("停车场内暂无车辆。")
                return None
            try:
                # 按车位查询车辆：
                if choice == 2:
                    keyword = int(input("请输入车位号："))
                    t_result = self.check_car(keyword, sort=1)
                    if t_result:
                        print("车位    车牌号     车型       颜色    入场时间 ")
                        print(t_result)
                        return t_result
                    else:
                        print("停车场中无此车辆。")

                # 按车牌查询车辆：
                elif choice == 3:
                    keyword = input("请输入车牌号：")
                    t_result = self.check_car(keyword, sort=2)
                    if t_result:
                        print("车位    车牌号     车型       颜色    入场时间 ")
                        print(t_result)
                        return t_result
                    else:
                        print("停车场中无此车辆。")

                # 按车型查询车辆：
                elif choice == 4:
                    keyword = Model(int(input("请输入车辆的车型（1小汽车, 2小卡, 3中卡, 4大卡）：")))
                    t_result = self.check_car(keyword, sort=3)
                    if t_result:
                        self.display(t_result)
                    else:
                        print("停车场中无此车型车辆。")

                # 按颜色查询车辆：
                elif choice == 5:
                    keyword = Color(int(input("请输入车辆的颜色（1白色, 2黑色, 3灰色, 4蓝色, 5红色, 6黄色）：")))
                    t_result = self.check_car(keyword, sort=4)
                    if t_result:
                        self.display(t_result)
                    else:
                        print("停车场中无此颜色车辆。")

                # 按入场时间查询：
                elif choice == 6:
                    # TODO (developing) 按入场时间查询
                    pass
                    """
                    keyword = input("请输入入场时间：")
                    t_result = self.check_car(keyword, sort=5)
                    if t_result:
                        print(t_result)
                    else:
                        print("停车场中无此车辆。")
                    """
                else:
                    pass
            except Exception as e:  # 输入异常处理
                # logging.exception(e)  # DEBUG
                print("输入错误，按任意键返回......")
                return None

    def pickup(self):
        """
        取车
        :return:None
        """
        if len(self.carlist) == 0:
            print("停车场内暂无车辆。")
            return None
        # 变量初始化
        exit_car = None
        inquire_choice = -1
        while inquire_choice < 0 or inquire_choice > 2:
            try:
                print("-----------取车-----------")
                inquire_choice = int(input("1)按车位查找\n2)按车牌号查找\n0)返回主菜单\n\n请输入操作码:"))
            except:
                continue
        if inquire_choice == 0:  # 返回主菜单
            return None
        elif inquire_choice == 1:  # 按车位
            exit_car = self.inquire(choice=2)
        elif inquire_choice == 2:  # 按车牌号
            exit_car = self.inquire(choice=3)
        if exit_car is None:
            return None
        exit_choice = input("确定请输入“Y”，其他任意输入返回主菜单：")
        if exit_choice == 'Y' or exit_choice == 'y':
            exit_time = time.ctime()
            park_time = time.mktime(time.strptime(exit_time)) - time.mktime(time.strptime(exit_car.intime))
            m, s = divmod(park_time, 60)
            h, m = divmod(m, 60)
            str_time = "%02d:%02d:%02d" % (h, m, s)  # 得到时分秒字符串
            global unit_price
            price = h * unit_price
            print("车牌号：%s \n停车时长：%s\n请交费%3d元 " % (exit_car.carnum, str_time, price))
            self.carlist.remove(exit_car)
            os.system("pause")  # 预留之后完善计费功能
            print("结算成功，欢迎您再次光临！")
        else:
            return None

    def edit(self):
        """
        编辑车辆信息
        :return:None
        """
        if len(self.carlist) == 0:
            print("停车场内暂无车辆。")
            return None

        # 变量初始化
        edit_car = None
        inquire_choice = -1
        while inquire_choice < 0 or inquire_choice > 2:
            try:
                print("-----车辆信息编辑-----")
                inquire_choice = int(input("1)按车位查找\n2)按车牌号查找\n0)返回主菜单\n\n请输入操作码:"))
            except:
                continue
        if inquire_choice == 0:  # 返回主菜单
            return None
        elif inquire_choice == 1:  # 按车位
            edit_car = self.inquire(choice=2)
        elif inquire_choice == 2:  # 按车牌号
            edit_car = self.inquire(choice=3)
        if edit_car is None:
            return None
        edit_choice = input("确定请输入“Y”，其他任意输入返回主菜单：")
        if edit_choice == 'Y' or edit_choice == 'y':
            index = self.carlist.index(edit_car)  # 获取索引
            while True:
                try:
                    flag_right = False  # right flag
                    change_choice = input("\n1)车位号\n2)车牌号\n3)车型\n4)车颜色\n5)入场时间\n0)不修改返回主菜单\n\n请输入您要修改的信息序号：")
                    if change_choice == '0':
                        return None
                    elif change_choice == '1':
                        new_info = int(input("请输入新的车位号："))
                        if 0 <= new_info <= self.max_car:  # 在范围内
                            for parkedCar in self.carlist:
                                if parkedCar.parknum == new_info:  # 判断车位是否已被占用
                                    print(" %d号车位已被占用！" % new_info)
                                    break
                            else:
                                self.carlist[index]["parknum"] = new_info
                                flag_right = True
                                print("车位号修改成功！")
                                # break
                    elif change_choice == '2':
                        new_info = input("请输入新的车牌号：")
                        if self.check_car_num(new_info):  # 判断车牌号是否有效
                            for parkedCar in self.carlist:
                                if parkedCar.carnum == new_info:  # 判断车牌是否已重复
                                    print("车牌号重复！")
                                    break
                            else:
                                self.carlist[index]["carnum"] = new_info
                                flag_right = True
                                print("车牌号修改成功！")
                                # break
                    elif change_choice == '3':
                        new_info = int(input("请输入新的车型（1小汽车, 2小卡, 3中卡, 4大卡）:"))
                        if 1 <= new_info <= 4:
                            new_info = Model(new_info)  # 转化为Model枚举类型
                            self.carlist[index]["model"] = new_info
                            flag_right = True
                            print("车型修改成功！")
                    elif change_choice == '4':
                        new_info = int(input("请输入新的车颜色（1白色, 2黑色, 3灰色, 4蓝色, 5红色, 6黄色）："))
                        if 1 <= new_info <= 6:
                            new_info = Color(new_info)  # 转化Color枚举类型
                            self.carlist[index]["color"] = new_info
                            flag_right = True
                            print("颜色修改成功！")
                    elif change_choice == '5':
                        new_info = input("请输入新的入场时间：(参考格式：2019.3.4 12:00:00)")
                        print("DEVELOPING...")
                        # TODO 修改入场时间
                        pass
                        break
                    else:
                        pass
                except:
                    print("输入错误，请重试！")
                    continue

                if flag_right:
                    break
                else:
                    print("请重试！")
                    continue
        else:
            return None

    def statistics(self):
        """
        统计车辆信息
        :return:None
        """
        print("""
        本停车场总车位数：{total:3d}  
        当前已驶入车辆数：{exist:3d}    空闲车位数：{empty:3d}
        -----------------------------------------------
        """.format(total=self.max_car, exist=len(self.carlist), empty=self.max_car-len(self.carlist)),
              end='')

        # 按车型、颜色统计车辆信息
        cnt_model = [0, 0, 0, 0]
        cnt_color = [0, 0, 0, 0, 0, 0]
        if len(self.carlist) != 0:
            for parkedCar in self.carlist:
                cnt_model[parkedCar.model.value-1] += 1
                cnt_color[parkedCar.color.value-1] += 1
        print("""
        * 按车型统计：
            小汽车 {:3d}, 小卡 {:3d}, 中卡 {:3d}, 大卡 {:3d}
        
        * 按颜色统计：
            白色 {:3d},  黑色 {:3d},  灰色 {:3d}
            蓝色 {:3d},  红色 {:3d},  黄色 {:3d} 
        """.format(cnt_model[0], cnt_model[1], cnt_model[2], cnt_model[3],
                   cnt_color[0], cnt_color[1], cnt_color[2],
                   cnt_color[3], cnt_color[4], cnt_color[5], ), end='')

        if len(self.carlist) == 0:
            print("""
        -----------------------------------------------
                """)
        else:
            # TODO 按入场时间统计
            print("""
        * 按入场时间统计：
            （正在开发中 Developing...）
        
        -----------------------------------------------""")

            # TODO 车辆信息按顺序输出

            # choice = input("""
            # 1)按车位排序  2)按入场时间排序
            # 请输入操作码（其他任意输入返回主菜单）:""")
            # if choice == '1':
            #     pass
            #     temp_carlist = []
            #     for parkedCar in self.carlist:
            #         pass
            #
            #     self.display(temp_carlist)
            # elif choice == '2':
            #     pass
            # else:
            #     return None
            #
