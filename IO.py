# -*- coding: utf-8 -*-
"""
# IO.py
Configurations of IO.
对于文件IO（等）的处理。
Made by Hzj.
"""

import multiprocessing as mp
from Car import Car, Model, Color


def load_from_file(park, filename=r"cars.csv"):
    """
    从文件中读取车辆信息。
    :param park:停车场实例
    :param filename:文件名
    :return: {class ParkManage}park, {int}cnt:导入成功计数
    """
    cnt = 0  # counter
    try:
        with open(filename, 'r+') as fp:

            while True:
                temp_car = fp.readline()
                if temp_car == '':
                    break
                else:
                    items = list(temp_car.strip().split(','))
                    car = Car(int(items[0]), items[1], Model(int(items[2])), Color(int(items[3])), items[4])
                    park.carlist.append(car)
                    cnt += 1
    except Exception:
        print('File loaded error!')
    return park, cnt


def load_new_file(park):
    """
    从新文件中加载记录，成功返回加载后的park，否则返回原来的park
    注意：此处暂未考虑重复记录及记录的有效性！
    :param park:停车场实例
    :return: {class ParkManage}park
    """
    filename = input('请输入导入的文件名（请勿重复导入）：')
    if filename == '':
        print('文件名不能为空！')
        return park
    elif filename == 'cars.csv':
        print('请勿导入重复文件！')
        return park
    else:
        temp_park, cnt_success = load_from_file(park=park, filename=filename)
        if cnt_success > 0:
            print('成功导入 %d 条记录。' % cnt_success)
            return temp_park
        else:
            print('导入失败！')
            return park


def write_to_file(park, filename=r"cars.csv"):
    """
    将车辆信息写入文件。
    :param park:停车场实例
    :param filename:文件名
    :return: None
    """
    try:
        with open(filename, 'w+') as file:
            if len(park.carlist) == 0:
                pass
            for parkedCar in park.carlist:
                file.write('{},{},{},{},{}\n'.format(parkedCar.parknum, parkedCar.carnum, parkedCar.model.value,
                                                     parkedCar.color.value, parkedCar.intime))
    except Exception:
        print('File wrote error!')


def realtimeIO():
    """
    TODO 实时读写文件
    思路：子进程每隔一段时间检查一次self.carlist，发现改动则更新文件。
    :return: None
    """
    pass
