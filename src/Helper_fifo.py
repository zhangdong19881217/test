#该模块用来解析stm32的hex文件
import re
import os
from typing import Sized
class CHelper_fifo(object):

    def __init__(self): 
        pass 
    
    '''获取Hex版本'''
    def fifoInit(self):
        buff = []
        return buff
    '''读取FIFO内容'''
    def fifoRead(self,buff):
        cRet = 1
        if len(buff) == 0:
            cRet = 0
        else:
            dat = list.pop([0]) 
        return cRet,dat
    '''写FIFO内容'''
    def fifoWrite(self,buff,dat):
        cRet = 1
        buff.append(dat)
        return cRet











                    