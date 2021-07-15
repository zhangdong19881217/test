from PyQt5 import QtCore, QtGui, QtWidgets

class CHelper_TextEdit(object):
    def __init__(self): 
        pass 
    #################################################################################
    #初始化COMBOX标签
    #str_name 控件名称
    #str  需要显示的内容
    #################################################################################
    def  SetText(self,str_name,str):
        mTextEdit = self.findChild(QtWidgets.QTextEdit, str_name) 
        mTextEdit.setText(str)
    #追加显示
    def SetText1(self,str_name,str):
        mTextEdit = self.findChild(QtWidgets.QTextEdit, str_name) 
        mTextEdit.append(str)