from ui import Ui_MainWindow
from ConnectSock import ConnectRobot
import time
import threading
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem,QHeaderView,QLineEdit,QItemDelegate,QVBoxLayout,QTableWidget,QWidget
from PyQt5.QtGui import QPixmap, QImage, QColor,QPainter, QPen,QDoubleValidator
from PyQt5.QtCore import pyqtSignal, pyqtSlot,QRect, Qt,QObject,QThread
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    

 
    
   #region Setup
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.Btn_Connect.clicked.connect(self.UseCamera)
        self.Btn_Inspect.clicked.connect(self.Run)

    def Connect_Camera(self,IP,Port):
        Robot = ConnectRobot(IP,Port)
        Time_Start = time.time() 
        Robot.send_data("Run")
        msg = Robot.get_data()
        print("msg "+ msg)
        Robot.close_socket()
        Cyctime = time.time() - Time_Start
        print("Cyctime", Cyctime * 10 ," msec")
    def UseCamera(self):
        self.Connect_Camera(self.IP_Server.text(),int(self.Port.text()))
        print("IP is  {} Port is {} ".format(self.IP_Server.text(),self.Port.text()))
    def Inspecttion(self):
        while True:
            self.UseCamera()
    def Run(self):
        self.t1 = threading.Thread(target=self.Inspecttion)
        self.t1.daemon = True
        self.t1.start()







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

        