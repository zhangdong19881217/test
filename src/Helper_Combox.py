
from PyQt5 import QtCore, QtGui, QtWidgets
class CHelper_Combox(object):
    #################################################################################
    #初始化COMBOX标签
    #str  combox 的名称
    #infomation = ["我想静静", "我要开始学习了", "我要开始睡觉了", "我要开始装B了"]
    #################################################################################
    def  ComboxInit(self,str,infomation):
         combox = self.findChild(QtWidgets.QComboBox, str)
         combox.addItems(infomation)
    #################################################################################
    #初始化COMBOX标签
    #str  combox 的名称
    #name string 类型，需要添加的标签
    #################################################################################
    def  ComboxInit1(self,str,name):
         combox = self.findChild(QtWidgets.QComboBox, str) 
         combox.addItem(name)
    #################################################################################
    #设置默认值
    #str  combox 的名称
    #combox.setCurrentIndex(0)
    #################################################################################
    def ComboxSetDefual(self,str,index):
        combox = self.findChild(QtWidgets.QComboBox, str) 
        combox.setCurrentIndex(index)
     #################################################################################
    #清空combox
    #str  combox 的名称
    #combox.setCurrentIndex(0)
    #################################################################################
    def ComboxClear(self,SelfWin):
        SelfWin.comboBox.clear()
        #combox = self.findChild(QtWidgets.QComboBox, str)
        #combox.clear(self)
