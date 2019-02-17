"""
# IO.py
Configurations of IO.
对于文件IO（等）的处理。
Made by Hzj.
"""

import multiprocessing as mp

def load_from_file(filename):
    """
    从文件中读取车辆信息。
    :param filename:文件名
    :return: None
    """
    with open(filename, 'r') as file:
        file.readline()
        pass
    # developing!!!!!!!!!!!!!!!!!!!!!!!!

def write_to_file(filename):
    """
    将车辆信息写入文件。
    :param filename:文件名
    :return: None
    """
    with open(filename, 'w') as file:
        file.write('')
        pass
    # developing!!!!!!!!!!!!!!!!!!!!!!!!

def realtimeIO():
    """
    实时读写文件，思路：子进程每隔一段时间检查一次self.carlist，发现改动则更新文件。
    :return: None
    """
    pass
    # developing!!!!!!!!!!!!!!!!!!!!!!!!
