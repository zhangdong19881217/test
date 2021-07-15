import re
from PyQt5 import QtCore, QtGui, QtWidgets
class CHelper_string(object):
    def __init__(self):
        pass
    '''
    获取两个字符串中间的字符   蓝牙链接上的标准串行 (COM17)
    CHelper_string.getStr(self,strCom,'\(','\)')
    '''
    def getStr(self,str, str1, str2):
        re1 = str1+'(.*?)'+str2
        reResult = re.findall(re1, str)
        return reResult[0]
        pass