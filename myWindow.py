
import sys
import threading

from PyQt5.QtGui import QIcon

from qt import *
from src.Helper_Serial import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from src.Helper_Log import *
from src.Helper_Combox import *
from src.Helper_Serial import *
from src.Helper_string import *
from src.Helper_Serial import *
#主窗口
class myWindow(QMainWindow, Ui_MainWindow):
    mySerial = None#串口句柄
    buff = []#串口读取FIFO的相关参数
    list0 = []#存储串口号
    list1 = []#存储串口号+详细信息
    def __init__(self, parent=None):
        super(myWindow, self).__init__(parent)
        self.setupUi(self)
        #设置图标
        self.setWindowIcon(QIcon("2.ico"))
        #设置软件显示名称
        self.setWindowTitle("test")
        #更新combox
        self.UpdateComBox()
        # 禁止调整窗口大小
        self.setFixedSize(self.width(), self.height())
    #-------------窗口事件---------------------------------------------------
    '''关闭窗口事件'''
    def closeEvent(self, e):
        self.closeCom()
    '''打开串口事件'''
    def onComOpen(self):
        if self.mySerial == None:
            self.openCom()
        elif self.mySerial.is_open:
            self.closeCom()
        else:
            self.openCom()
        pass

    '''编辑框发生改变事'''
    def ontextEdit(self):

        pass
    '''更新串口'''
    def onUpdateCom(self):
        self.UpdateComBox()
        pass
    
    '''清空编辑'''
    def onClear(self):
        self.textEdit.setText("")
        buff = [0,1,2,3,4,5,6,7,8,9]
        CHelper_Serial.sendBytes(self,self.mySerial, buff)
    #----------------------------------------------------------------
    '''更新串口号及波特率'''
    def UpdateComBox(self):
        self.comboBox.clear()
        self.list0,self.list1 = CHelper_Serial.GetPortName(self)
        self.comboBox.addItems(self.list1)

        listBaud = ["115200","9600"]
        self.comboBox_2.clear()
        self.comboBox_2.addItems(listBaud)

    '''开启串口'''
    def openCom(self):
        try:
            #读取串口号
            #strCom = self.comboBox.currentText()
            index = self.comboBox.currentIndex()
            strCom = self.list0[index]
            #strCom = CHelper_string.getStr(self,strCom,'\(','\)')
            #读取波特率
            strBaud = self.comboBox_2.currentText()
            #清空FIFO
            self.buff.clear()
            #打开串口
            myCOM =CHelper_Serial()
            self.mySerial,self.isOpen,self.buff = myCOM.openCom(strCom,strBaud)
            if self.isOpen:
                self.showLog('串口打开成功:'+strCom+' '+strBaud)
                self.pushButton_3.setText('关闭')
            else:
                self.showLog('串口打开失败')
                self.pushButton_3.setText('打开')
        except Exception as e:
            pass
    '''关闭串口'''
    def closeCom(self):
        try:
            if self.mySerial != None:
                CHelper_Serial.closeSerial(self,self.mySerial)
                self.pushButton_3.setText('打开')
        except Exception as e:
            #print('异常：',e)
            pass
        self.showLog('串口关闭')
    #打印log color = 0  黑色显示    color = 1  红色显示
    def showLog(self,str, color=0):
        if (color == 1):
            self.textEdit.append("<font color=\"#FF0000\">" + str + "</font> ")
        else:
            self.textEdit.append(str)

    



