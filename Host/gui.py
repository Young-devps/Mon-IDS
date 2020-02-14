# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!
import sys
import pandas as pd
import ast
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, QPushButton
from PyQt5.QtGui import QIcon
import random

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.gridspec as GridSpec
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib import style
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar




class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'Agents Monitoring #techcodefacil Bayo'
        self.width = 640
        self.height = 400

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(942, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.actualTime = QtWidgets.QLCDNumber(self.centralwidget)
        self.actualTime.setGeometry(QtCore.QRect(870, 40, 64, 23))
        self.actualTime.setObjectName("actualTime")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 161, 17))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(850, 10, 91, 20))
        self.label_3.setObjectName("label_3")
        self.connectBAr = QtWidgets.QProgressBar(self.centralwidget)
        self.connectBAr.setGeometry(QtCore.QRect(110, 70, 118, 23))
        self.connectBAr.setProperty("value", 24)
        self.connectBAr.setObjectName("connectBAr")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 70, 101, 29))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(260, 50, 301, 191))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(160, 80, 67, 17))
        self.label_2.setStyleSheet("font: italic 11pt \"Ubuntu\";")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 151, 31))
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(150, 20, 131, 31))
        self.label_5.setStyleSheet("font: italic 11pt \"Ubuntu\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(20, 26, 81, 21))
        self.label_6.setStyleSheet("\n""")
        self.label_6.setObjectName("label_6")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 71, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(10, 60, 91, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(10, 90, 121, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(10, 130, 81, 17))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(170, 20, 161, 17))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(170, 60, 121, 17))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(170, 90, 67, 17))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(170, 130, 67, 17))
        self.label_14.setObjectName("label_14")
        self.tabWidget.addTab(self.tab_2, "")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(570, 50, 251, 191))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(0, 20, 67, 17))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setGeometry(QtCore.QRect(50, 20, 191, 20))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(0, 60, 91, 17))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab_3)
        self.label_18.setGeometry(QtCore.QRect(100, 60, 67, 17))
        self.label_18.setObjectName("label_18")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_19 = QtWidgets.QLabel(self.tab_4)
        self.label_19.setGeometry(QtCore.QRect(0, 20, 67, 17))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab_4)
        self.label_20.setGeometry(QtCore.QRect(80, 20, 67, 17))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.tab_4)
        self.label_21.setGeometry(QtCore.QRect(0, 60, 67, 17))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.tab_4)
        self.label_22.setGeometry(QtCore.QRect(80, 60, 121, 17))
        self.label_22.setObjectName("label_22")
        self.tabWidget_2.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 942, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionClose_App = QtWidgets.QAction(MainWindow)
        self.actionClose_App.setObjectName("actionClose_App")
        self.actionEdit_IP = QtWidgets.QAction(MainWindow)
        self.actionEdit_IP.setObjectName("actionEdit_IP")
        self.actionedit_port = QtWidgets.QAction(MainWindow)
        self.actionedit_port.setObjectName("actionedit_port")
        self.actionDocumentation = QtWidgets.QAction(MainWindow)
        self.actionDocumentation.setObjectName("actionDocumentation")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionClose_App)
        self.menuEdit.addAction(self.actionEdit_IP)
        self.menuEdit.addAction(self.actionedit_port)
        self.menuHelp.addAction(self.actionDocumentation)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        MainWindow.setWindowTitle(self.title)
        MainWindow.setGeometry(self.left, self.top, self.width, self.height)

        m = PlotCanvas(MainWindow, width=7, height=4.5)
        m.move(20,270)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Server"))
        self.label_3.setText(_translate("MainWindow", "12/12/2019"))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>clik to open server port</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Run server"))
        self.label_2.setText(_translate("MainWindow", "77.0 %"))
        self.label_4.setText(_translate("MainWindow", "percentage:"))
        self.label_5.setText(_translate("MainWindow", "5125/8201 MB    "))
        self.label_6.setText(_translate("MainWindow", "using:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "MEMORY"))
        self.label_7.setText(_translate("MainWindow", "Clock:"))
        self.label_8.setText(_translate("MainWindow", "User-usage:"))
        self.label_9.setText(_translate("MainWindow", "System-usage: "))
        self.label_10.setText(_translate("MainWindow", "Idle-usage: "))
        self.label_11.setText(_translate("MainWindow", "1.13 Ghz/2.48 Ghz    "))
        self.label_12.setText(_translate("MainWindow", "14.2%"))
        self.label_13.setText(_translate("MainWindow", "41.4%    "))
        self.label_14.setText(_translate("MainWindow", "36.3%    "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "CPU"))
        self.label_15.setText(_translate("MainWindow", "using: "))
        self.label_16.setText(_translate("MainWindow", "    138.75/317.49 GB    "))
        self.label_17.setText(_translate("MainWindow", "percentage: "))
        self.label_18.setText(_translate("MainWindow", "20.6 %"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "STORAGE"))
        self.label_19.setText(_translate("MainWindow", "local"))
        self.label_20.setText(_translate("MainWindow", "127.0.0.1"))
        self.label_21.setText(_translate("MainWindow", "outer"))
        self.label_22.setText(_translate("MainWindow", "41.202.219.245"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "IP ADDR"))
        self.menuFile.setTitle(_translate("MainWindow", "Fi&le"))
        self.menuEdit.setTitle(_translate("MainWindow", "E&dit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help?"))
        self.actionNew.setText(_translate("MainWindow", "&New"))
        self.actionSave.setText(_translate("MainWindow", "&Save"))
        self.actionClose_App.setText(_translate("MainWindow", "&Close App"))
        self.actionEdit_IP.setText(_translate("MainWindow", "&Edit \'IP\'"))
        self.actionedit_port.setText(_translate("MainWindow", "edit &port"))
        self.actionDocumentation.setText(_translate("MainWindow", "&Documentation"))


class PlotCanvas(FigureCanvas):

    
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()
        


    def plot(self):
        val  = pd.read_csv("monitorDB.csv")

        data = [random.random() for i in range(25)]

        ax2 = self.figure.add_subplot(222)
        ax2.plot(data, 'r-')
        ax2.set_title('MEMORY')
        ax2.grid(True)
        memory_used = [f(x, "tuple") for x in val['RAM[3]-used']]
        memory_total, byte =  parse_tuple(val['RAM[0]-total'])
        cols = ['b','y']
        date = [f(x, "date") for x in val['datetime']]
        ax2.plot(date, memory_used, label='cpu user')
        ax2.plot(date, memory_total, label='cpu system')
        plt.xlabel('dates')
        plt.ylabel('memory')
        ax2.legend()

        ax3 = self.figure.add_subplot(223)
        ax3.set_title('DISK')
        Disk_used = [f(x, "tuple") for x in val['Disk[1]-used']]
        Disk_total, byte =  parse_tuple(val['Disk[0]-total'].max())
        slices =[float(Disk_used[-1]), float(Disk_total)]
        activities = ['Disk_used', 'Disk_total']
        cols = ['b','y']
        ax3.pie(slices, labels=activities, colors=cols, explode=(0,0.1), startangle=90, shadow=True, autopct='%1.1f%%')
        ax3.legend()


        ax4 = self.figure.add_subplot(224)
        ax4.plot(data, 'r-')
        ax4.set_title('TEMP')
        ax4.grid(True)

        style.use('dark_background')
        ax1 = self.figure.add_subplot(221)
        ax1.set_title('CPU')
        cputp_user = [f(x, "float") for x in val['cputp[0]-user']]
        cputp_system = [f(x, "float") for x in val['cputp[1]-system']]
        cputp_idle = [f(x, "float") for x in val['cputp[2]-Idle']]
        date = [f(x, "date") for x in val['datetime']]
        ax1.plot(date, cputp_user, label='cpu user')
        ax1.plot(date, cputp_system, label='cpu system')
        ax1.plot(date, cputp_idle, label='cpu idle')
        plt.xlabel('dates')
        plt.ylabel('utils')
        ax1.legend()
        
        #self.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
       

        self.draw()









def parse_tuple(string):
    try:
        s = ast.literal_eval(str(string))
        if type(s) == tuple:
            return s
        return
    except:
        return
    
    
def f(x, type_):
    if type_ =="float":
        x = float(x)
        return x
    elif type_ == "tuple":
        x = parse_tuple(x)
        size, byte = x
        return size
    elif type_ == "date":
        arr = x.split(".")
        return arr[0]




import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
screen = Ui_MainWindow()
screen.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())