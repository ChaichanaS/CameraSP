# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConnectCamera.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(240, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 241, 311))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.IP_Server = QtWidgets.QLineEdit(self.tab)
        self.IP_Server.setGeometry(QtCore.QRect(40, 10, 131, 32))
        self.IP_Server.setObjectName("IP_Server")
        self.Port = QtWidgets.QLineEdit(self.tab)
        self.Port.setGeometry(QtCore.QRect(40, 60, 131, 32))
        self.Port.setObjectName("Port")
        self.Btn_Connect = QtWidgets.QPushButton(self.tab)
        self.Btn_Connect.setGeometry(QtCore.QRect(60, 110, 99, 30))
        self.Btn_Connect.setObjectName("Btn_Connect")
        self.Btn_Inspect = QtWidgets.QPushButton(self.tab)
        self.Btn_Inspect.setGeometry(QtCore.QRect(60, 170, 99, 30))
        self.Btn_Inspect.setObjectName("Btn_Connect")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 221, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Btn_Connect.setText(_translate("MainWindow", "Connect.."))
        self.Btn_Inspect.setText(_translate("MainWindow", "Inspec"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Connect Camera"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Data Table"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

