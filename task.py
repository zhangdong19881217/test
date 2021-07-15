from  myWindow import *
from PyQt5.QtWidgets import QApplication, QMainWindow

class task(object):
    def __init__(self):
        pass
    def run(self):
        app = QApplication(sys.argv)
        myWin = myWindow()
        myWin.show()
        sys.exit(app.exec_())

