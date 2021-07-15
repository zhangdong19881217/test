
from PyQt5 import QtCore, QtGui, QtWidgets
class CHelper_log(object):
    def __init__(self):
        pass
    '''
    默认黑色
    color = 0  黑色显示
    color = 1  红色显示
    '''
    def ShowLog(self,strTextEdit, str, color = 0):
        MytextEdit = self.findChild(QtWidgets.QTextEdit, strTextEdit)
        if (color == 1):
            MytextEdit.append("<font color=\"#FF0000\">" + str + "</font> ")
        else:
            MytextEdit.append(str)
    def ClrLog(self,strTextEdit):
        MytextEdit = self.findChild(QtWidgets.QTextEdit, strTextEdit)
        MytextEdit.setText('')