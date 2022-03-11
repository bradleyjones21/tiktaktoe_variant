# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tiktaktoe.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from playsound import playsound

squareIndex = [ 1,1,1,2,2,2,3,3,3,
                1,1,1,2,2,2,3,3,3,
                1,1,1,2,2,2,3,3,3,
                4,4,4,5,5,5,6,6,6,
                4,4,4,5,5,5,6,6,6,
                4,4,4,5,5,5,6,6,6,
                7,7,7,8,8,8,9,9,9,
                7,7,7,8,8,8,9,9,9,
                7,7,7,8,8,8,9,9,9]
squareIndex2 = [[1,2,3,10,11,12,19,20,21],
               [4,5,6,13,14,15,22,23,24],
               [7,8,9,16,17,18,25,26,27],
               [28,29,30,37,38,39,46,47,48],
               [31,32,33,40,41,42,49,50,51],
               [34,35,36,43,44,45,52,53,54],
               [55,56,57,64,65,66,73,74,75],
               [58,59,60,67,68,69,76,77,78],
               [61,62,63,70,71,72,79,80,81]]
squareMemory1 = [[False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False]]
squareMemory2 = [[False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False],
                 [False,False,False,False,False,False,False,False,False]]
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 774)
        self.turnCount=1
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(210, 190, 40, 40))
        self.pushButton_1.setText("")
        self.pushButton_1.clicked.connect(partial(self.click_button, 1))
        self.pushButton_1.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 190, 40, 40))
        self.pushButton_2.setText("")
        self.pushButton_2.clicked.connect(partial(self.click_button, 2))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 190, 40, 40))
        self.pushButton_3.setText("")
        self.pushButton_3.clicked.connect(partial(self.click_button, 3))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(330, 190, 40, 40))
        self.pushButton_4.setText("")
        self.pushButton_4.clicked.connect(partial(self.click_button, 4))
        self.pushButton_4.setStyleSheet("background-color:rgb(199,199,199)"+"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(370, 190, 40, 40))
        self.pushButton_5.setText("")
        self.pushButton_5.clicked.connect(partial(self.click_button, 5))
        self.pushButton_5.setStyleSheet("background-color:rgb(199,199,199);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(410, 190, 40, 40))
        self.pushButton_6.setText("")
        self.pushButton_6.clicked.connect(partial(self.click_button, 6))
        self.pushButton_6.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(450, 190, 40, 40))
        self.pushButton_7.setText("")
        self.pushButton_7.clicked.connect(partial(self.click_button, 7))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(490, 190, 40, 40))
        self.pushButton_8.setText("")
        self.pushButton_8.clicked.connect(partial(self.click_button, 8))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(530, 190, 40, 40))
        self.pushButton_9.setText("")
        self.pushButton_9.clicked.connect(partial(self.click_button, 9))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(210, 230, 40, 40))
        self.pushButton_10.setText("")
        self.pushButton_10.clicked.connect(partial(self.click_button, 10))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(250, 230, 40, 40))
        self.pushButton_11.setText("")
        self.pushButton_11.clicked.connect(partial(self.click_button, 11))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(290, 230, 40, 40))
        self.pushButton_12.setText("")
        self.pushButton_12.clicked.connect(partial(self.click_button, 12))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(330, 230, 40, 40))
        self.pushButton_13.setText("")
        self.pushButton_13.clicked.connect(partial(self.click_button, 13))
        self.pushButton_13.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(370, 230, 40, 40))
        self.pushButton_14.setText("")
        self.pushButton_14.clicked.connect(partial(self.click_button, 14))
        self.pushButton_14.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(410, 230, 40, 40))
        self.pushButton_15.setText("")
        self.pushButton_15.clicked.connect(partial(self.click_button, 15))
        self.pushButton_15.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(450, 230, 40, 40))
        self.pushButton_16.setText("")
        self.pushButton_16.clicked.connect(partial(self.click_button, 16))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(490, 230, 40, 40))
        self.pushButton_17.setText("")
        self.pushButton_17.clicked.connect(partial(self.click_button, 17))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(530, 230, 40, 40))
        self.pushButton_18.setText("")
        self.pushButton_18.clicked.connect(partial(self.click_button, 18))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(210, 270, 40, 40))
        self.pushButton_19.setText("")
        self.pushButton_19.clicked.connect(partial(self.click_button, 19))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(250, 270, 40, 40))
        self.pushButton_20.setText("")
        self.pushButton_20.clicked.connect(partial(self.click_button, 20))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(290, 270, 40, 40))
        self.pushButton_21.setText("")
        self.pushButton_21.clicked.connect(partial(self.click_button, 21))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(330, 270, 40, 40))
        self.pushButton_22.setText("")
        self.pushButton_22.clicked.connect(partial(self.click_button, 22))
        self.pushButton_22.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(370, 270, 40, 40))
        self.pushButton_23.setText("")
        self.pushButton_23.clicked.connect(partial(self.click_button, 23))
        self.pushButton_23.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(410, 270, 40, 40))
        self.pushButton_24.setText("")
        self.pushButton_24.clicked.connect(partial(self.click_button, 24))
        self.pushButton_24.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_25.setGeometry(QtCore.QRect(450, 270, 40, 40))
        self.pushButton_25.setText("")
        self.pushButton_25.clicked.connect(partial(self.click_button, 25))
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_26.setGeometry(QtCore.QRect(490, 270, 40, 40))
        self.pushButton_26.setText("")
        self.pushButton_26.clicked.connect(partial(self.click_button, 26))
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_27.setGeometry(QtCore.QRect(530, 270, 40, 40))
        self.pushButton_27.setText("")
        self.pushButton_27.clicked.connect(partial(self.click_button, 27))
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_28.setGeometry(QtCore.QRect(210, 310, 40, 40))
        self.pushButton_28.setText("")
        self.pushButton_28.clicked.connect(partial(self.click_button, 28))
        self.pushButton_28.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_29 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_29.setGeometry(QtCore.QRect(250, 310, 40, 40))
        self.pushButton_29.setText("")
        self.pushButton_29.clicked.connect(partial(self.click_button, 29))
        self.pushButton_29.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_30.setGeometry(QtCore.QRect(290, 310, 40, 40))
        self.pushButton_30.setText("")
        self.pushButton_30.clicked.connect(partial(self.click_button, 30))
        self.pushButton_30.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_31.setGeometry(QtCore.QRect(330, 310, 40, 40))
        self.pushButton_31.setText("")
        self.pushButton_31.clicked.connect(partial(self.click_button, 31))
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_32 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_32.setGeometry(QtCore.QRect(370, 310, 40, 40))
        self.pushButton_32.setText("")
        self.pushButton_32.clicked.connect(partial(self.click_button, 32))
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_33 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_33.setGeometry(QtCore.QRect(410, 310, 40, 40))
        self.pushButton_33.setText("")
        self.pushButton_33.clicked.connect(partial(self.click_button, 33))
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_34.setGeometry(QtCore.QRect(450, 310, 40, 40))
        self.pushButton_34.setText("")
        self.pushButton_34.clicked.connect(partial(self.click_button, 34))
        self.pushButton_34.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_35.setGeometry(QtCore.QRect(490, 310, 40, 40))
        self.pushButton_35.setText("")
        self.pushButton_35.clicked.connect(partial(self.click_button, 35))
        self.pushButton_35.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_36 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_36.setGeometry(QtCore.QRect(530, 310, 40, 40))
        self.pushButton_36.setText("")
        self.pushButton_36.clicked.connect(partial(self.click_button, 36))
        self.pushButton_36.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton_37 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_37.setGeometry(QtCore.QRect(210, 350, 40, 40))
        self.pushButton_37.setText("")
        self.pushButton_37.clicked.connect(partial(self.click_button, 37))
        self.pushButton_37.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_38 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_38.setGeometry(QtCore.QRect(250, 350, 40, 40))
        self.pushButton_38.setText("")
        self.pushButton_38.clicked.connect(partial(self.click_button, 38))
        self.pushButton_38.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_38.setObjectName("pushButton_38")
        self.pushButton_39 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_39.setGeometry(QtCore.QRect(290, 350, 40, 40))
        self.pushButton_39.setText("")
        self.pushButton_39.clicked.connect(partial(self.click_button, 39))
        self.pushButton_39.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_40 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_40.setGeometry(QtCore.QRect(330, 350, 40, 40))
        self.pushButton_40.setText("")
        self.pushButton_40.clicked.connect(partial(self.click_button, 40))
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_41 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_41.setGeometry(QtCore.QRect(370, 350, 40, 40))
        self.pushButton_41.setText("")
        self.pushButton_41.clicked.connect(partial(self.click_button, 41))
        self.pushButton_41.setObjectName("pushButton_41")
        self.pushButton_42 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_42.setGeometry(QtCore.QRect(410, 350, 40, 40))
        self.pushButton_42.setText("")
        self.pushButton_42.clicked.connect(partial(self.click_button, 42))
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_43 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_43.setGeometry(QtCore.QRect(450, 350, 40, 40))
        self.pushButton_43.setText("")
        self.pushButton_43.clicked.connect(partial(self.click_button, 43))
        self.pushButton_43.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_44 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_44.setGeometry(QtCore.QRect(490, 350, 40, 40))
        self.pushButton_44.setText("")
        self.pushButton_44.clicked.connect(partial(self.click_button, 44))
        self.pushButton_44.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_44.setObjectName("pushButton_44")
        self.pushButton_45 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_45.setGeometry(QtCore.QRect(530, 350, 40, 40))
        self.pushButton_45.setText("")
        self.pushButton_45.clicked.connect(partial(self.click_button, 45))
        self.pushButton_45.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_46 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_46.setGeometry(QtCore.QRect(210, 390, 40, 40))
        self.pushButton_46.setText("")
        self.pushButton_46.clicked.connect(partial(self.click_button, 46))
        self.pushButton_46.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_46.setObjectName("pushButton_46")
        self.pushButton_47 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_47.setGeometry(QtCore.QRect(250, 390, 40, 40))
        self.pushButton_47.setText("")
        self.pushButton_47.clicked.connect(partial(self.click_button, 47))
        self.pushButton_47.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_47.setObjectName("pushButton_47")
        self.pushButton_48 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_48.setGeometry(QtCore.QRect(290, 390, 40, 40))
        self.pushButton_48.setText("")
        self.pushButton_48.clicked.connect(partial(self.click_button, 48))
        self.pushButton_48.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_48.setObjectName("pushButton_48")
        self.pushButton_49 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_49.setGeometry(QtCore.QRect(330, 390, 40, 40))
        self.pushButton_49.setText("")
        self.pushButton_49.clicked.connect(partial(self.click_button, 49))
        self.pushButton_49.setObjectName("pushButton_49")
        self.pushButton_50 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_50.setGeometry(QtCore.QRect(370, 390, 40, 40))
        self.pushButton_50.setText("")
        self.pushButton_50.clicked.connect(partial(self.click_button, 50))
        self.pushButton_50.setObjectName("pushButton_50")
        self.pushButton_51 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_51.setGeometry(QtCore.QRect(410, 390, 40, 40))
        self.pushButton_51.setText("")
        self.pushButton_51.clicked.connect(partial(self.click_button, 51))
        self.pushButton_51.setObjectName("pushButton_51")
        self.pushButton_52 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_52.setGeometry(QtCore.QRect(450, 390, 40, 40))
        self.pushButton_52.setText("")
        self.pushButton_52.clicked.connect(partial(self.click_button, 52))
        self.pushButton_52.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_52.setObjectName("pushButton_52")
        self.pushButton_53 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_53.setGeometry(QtCore.QRect(490, 390, 40, 40))
        self.pushButton_53.setText("")
        self.pushButton_53.clicked.connect(partial(self.click_button, 53))
        self.pushButton_53.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_53.setObjectName("pushButton_53")
        self.pushButton_54 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_54.setGeometry(QtCore.QRect(530, 390, 40, 40))
        self.pushButton_54.setText("")
        self.pushButton_54.clicked.connect(partial(self.click_button, 54))
        self.pushButton_54.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_54.setObjectName("pushButton_54")
        self.pushButton_55 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_55.setGeometry(QtCore.QRect(210, 430, 40, 40))
        self.pushButton_55.setText("")
        self.pushButton_55.clicked.connect(partial(self.click_button, 55))
        self.pushButton_55.setObjectName("pushButton_55")
        self.pushButton_56 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_56.setGeometry(QtCore.QRect(250, 430, 40, 40))
        self.pushButton_56.setText("")
        self.pushButton_56.clicked.connect(partial(self.click_button, 56))
        self.pushButton_56.setObjectName("pushButton_56")
        self.pushButton_57 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_57.setGeometry(QtCore.QRect(290, 430, 40, 40))
        self.pushButton_57.setText("")
        self.pushButton_57.clicked.connect(partial(self.click_button, 57))
        self.pushButton_57.setObjectName("pushButton_57")
        self.pushButton_58 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_58.setGeometry(QtCore.QRect(330, 430, 40, 40))
        self.pushButton_58.setText("")
        self.pushButton_58.clicked.connect(partial(self.click_button, 58))
        self.pushButton_58.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_58.setObjectName("pushButton_58")
        self.pushButton_59 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_59.setGeometry(QtCore.QRect(370, 430, 40, 40))
        self.pushButton_59.setText("")
        self.pushButton_59.clicked.connect(partial(self.click_button, 59))
        self.pushButton_59.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_59.setObjectName("pushButton_59")
        self.pushButton_60 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_60.setGeometry(QtCore.QRect(410, 430, 40, 40))
        self.pushButton_60.setText("")
        self.pushButton_60.clicked.connect(partial(self.click_button, 60))
        self.pushButton_60.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_60.setObjectName("pushButton_60")
        self.pushButton_61 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_61.setGeometry(QtCore.QRect(450, 430, 40, 40))
        self.pushButton_61.setText("")
        self.pushButton_61.clicked.connect(partial(self.click_button, 61))
        self.pushButton_61.setObjectName("pushButton_61")
        self.pushButton_62 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_62.setGeometry(QtCore.QRect(490, 430, 40, 40))
        self.pushButton_62.setText("")
        self.pushButton_62.clicked.connect(partial(self.click_button, 62))
        self.pushButton_62.setObjectName("pushButton_62")
        self.pushButton_63 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_63.setGeometry(QtCore.QRect(530, 430, 40, 40))
        self.pushButton_63.setText("")
        self.pushButton_63.clicked.connect(partial(self.click_button, 63))
        self.pushButton_63.setObjectName("pushButton_63")
        self.pushButton_64 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_64.setGeometry(QtCore.QRect(210, 470, 40, 40))
        self.pushButton_64.setText("")
        self.pushButton_64.clicked.connect(partial(self.click_button, 64))
        self.pushButton_64.setObjectName("pushButton_64")
        self.pushButton_65 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_65.setGeometry(QtCore.QRect(250, 470, 40, 40))
        self.pushButton_65.setText("")
        self.pushButton_65.clicked.connect(partial(self.click_button, 65))
        self.pushButton_65.setObjectName("pushButton_65")
        self.pushButton_66 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_66.setGeometry(QtCore.QRect(290, 470, 40, 40))
        self.pushButton_66.setText("")
        self.pushButton_66.clicked.connect(partial(self.click_button, 66))
        self.pushButton_66.setObjectName("pushButton_66")
        self.pushButton_67 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_67.setGeometry(QtCore.QRect(330, 470, 40, 40))
        self.pushButton_67.setText("")
        self.pushButton_67.clicked.connect(partial(self.click_button, 67))
        self.pushButton_67.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_67.setObjectName("pushButton_67")
        self.pushButton_68 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_68.setGeometry(QtCore.QRect(370, 470, 40, 40))
        self.pushButton_68.setText("")
        self.pushButton_68.clicked.connect(partial(self.click_button, 68))
        self.pushButton_68.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_68.setObjectName("pushButton_68")
        self.pushButton_69 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_69.setGeometry(QtCore.QRect(410, 470, 40, 40))
        self.pushButton_69.setText("")
        self.pushButton_69.clicked.connect(partial(self.click_button, 69))
        self.pushButton_69.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_69.setObjectName("pushButton_69")
        self.pushButton_70 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_70.setGeometry(QtCore.QRect(450, 470, 40, 40))
        self.pushButton_70.setText("")
        self.pushButton_70.clicked.connect(partial(self.click_button, 70))
        self.pushButton_70.setObjectName("pushButton_70")
        self.pushButton_71 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_71.setGeometry(QtCore.QRect(490, 470, 40, 40))
        self.pushButton_71.setText("")
        self.pushButton_71.clicked.connect(partial(self.click_button, 71))
        self.pushButton_71.setObjectName("pushButton_71")
        self.pushButton_72 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_72.setGeometry(QtCore.QRect(530, 470, 40, 40))
        self.pushButton_72.setText("")
        self.pushButton_72.clicked.connect(partial(self.click_button, 72))
        self.pushButton_72.setObjectName("pushButton_72")
        self.pushButton_73 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_73.setGeometry(QtCore.QRect(210, 510, 40, 40))
        self.pushButton_73.setText("")
        self.pushButton_73.clicked.connect(partial(self.click_button, 73))
        self.pushButton_73.setObjectName("pushButton_73")
        self.pushButton_74 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_74.setGeometry(QtCore.QRect(250, 510, 40, 40))
        self.pushButton_74.setText("")
        self.pushButton_74.clicked.connect(partial(self.click_button, 74))
        self.pushButton_74.setObjectName("pushButton_74")
        self.pushButton_75 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_75.setGeometry(QtCore.QRect(290, 510, 40, 40))
        self.pushButton_75.setText("")
        self.pushButton_75.clicked.connect(partial(self.click_button, 75))
        self.pushButton_75.setObjectName("pushButton_75")
        self.pushButton_76 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_76.setGeometry(QtCore.QRect(330, 510, 40, 40))
        self.pushButton_76.setText("")
        self.pushButton_76.clicked.connect(partial(self.click_button, 76))
        self.pushButton_76.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_76.setObjectName("pushButton_76")
        self.pushButton_77 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_77.setGeometry(QtCore.QRect(370, 510, 40, 40))
        self.pushButton_77.setText("")
        self.pushButton_77.clicked.connect(partial(self.click_button, 77))
        self.pushButton_77.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_77.setObjectName("pushButton_77")
        self.pushButton_78 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_78.setGeometry(QtCore.QRect(410, 510, 40, 40))
        self.pushButton_78.setText("")
        self.pushButton_78.clicked.connect(partial(self.click_button, 78))
        self.pushButton_78.setStyleSheet("background-color:rgb(199,199,199)")
        self.pushButton_78.setObjectName("pushButton_78")
        self.pushButton_79 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_79.setGeometry(QtCore.QRect(450, 510, 40, 40))
        self.pushButton_79.setText("")
        self.pushButton_79.clicked.connect(partial(self.click_button, 79))
        self.pushButton_79.setObjectName("pushButton_79")
        self.pushButton_80 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_80.setGeometry(QtCore.QRect(490, 510, 40, 40))
        self.pushButton_80.setText("")
        self.pushButton_80.clicked.connect(partial(self.click_button, 80))
        self.pushButton_80.setObjectName("pushButton_80")
        self.pushButton_81 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_81.setGeometry(QtCore.QRect(530, 510, 40, 40))
        self.pushButton_81.setText("")
        self.pushButton_81.clicked.connect(partial(self.click_button, 81))
        self.pushButton_81.setObjectName("pushButton_81")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 10, 361, 181))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo2.PNG"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, -20, 801, 771))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("elegant-white-background-with-shiny-lines_1017-17580.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.pushButton_1.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        self.pushButton_11.raise_()
        self.pushButton_12.raise_()
        self.pushButton_13.raise_()
        self.pushButton_14.raise_()
        self.pushButton_15.raise_()
        self.pushButton_16.raise_()
        self.pushButton_17.raise_()
        self.pushButton_18.raise_()
        self.pushButton_19.raise_()
        self.pushButton_20.raise_()
        self.pushButton_21.raise_()
        self.pushButton_22.raise_()
        self.pushButton_23.raise_()
        self.pushButton_24.raise_()
        self.pushButton_25.raise_()
        self.pushButton_26.raise_()
        self.pushButton_27.raise_()
        self.pushButton_28.raise_()
        self.pushButton_29.raise_()
        self.pushButton_30.raise_()
        self.pushButton_31.raise_()
        self.pushButton_32.raise_()
        self.pushButton_33.raise_()
        self.pushButton_34.raise_()
        self.pushButton_35.raise_()
        self.pushButton_36.raise_()
        self.pushButton_37.raise_()
        self.pushButton_38.raise_()
        self.pushButton_39.raise_()
        self.pushButton_40.raise_()
        self.pushButton_41.raise_()
        self.pushButton_42.raise_()
        self.pushButton_43.raise_()
        self.pushButton_44.raise_()
        self.pushButton_45.raise_()
        self.pushButton_46.raise_()
        self.pushButton_47.raise_()
        self.pushButton_48.raise_()
        self.pushButton_49.raise_()
        self.pushButton_50.raise_()
        self.pushButton_51.raise_()
        self.pushButton_52.raise_()
        self.pushButton_53.raise_()
        self.pushButton_54.raise_()
        self.pushButton_55.raise_()
        self.pushButton_56.raise_()
        self.pushButton_57.raise_()
        self.pushButton_58.raise_()
        self.pushButton_59.raise_()
        self.pushButton_60.raise_()
        self.pushButton_61.raise_()
        self.pushButton_62.raise_()
        self.pushButton_63.raise_()
        self.pushButton_64.raise_()
        self.pushButton_65.raise_()
        self.pushButton_66.raise_()
        self.pushButton_67.raise_()
        self.pushButton_68.raise_()
        self.pushButton_69.raise_()
        self.pushButton_70.raise_()
        self.pushButton_71.raise_()
        self.pushButton_72.raise_()
        self.pushButton_73.raise_()
        self.pushButton_74.raise_()
        self.pushButton_75.raise_()
        self.pushButton_76.raise_()
        self.pushButton_77.raise_()
        self.pushButton_78.raise_()
        self.pushButton_79.raise_()
        self.pushButton_80.raise_()
        self.pushButton_81.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 550, 600, 120))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 550, 600, 120))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" color:#ffc0cb;\">Player 2\'s Turn</span></p></body></html>"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" color:#ff0000;\">Player 1\'s Turn</span></p></body></html>"))
        self.label_3.hide()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def check_for_complete(self, player1, square, row, column):
        if player1:
            checkArray = squareMemory1[square-1]
        else:
            checkArray = squareMemory2[square-1]
        print(row)
        print(column)
        temp = 3*row+column
        checkArray[temp]=True
        print(checkArray)
        l1=checkArray[0]&checkArray[1]&checkArray[2]
        l2=checkArray[0]&checkArray[3]&checkArray[6]
        l3=checkArray[0]&checkArray[4]&checkArray[8]
        l4=checkArray[1]&checkArray[4]&checkArray[7]
        l5=checkArray[3]&checkArray[4]&checkArray[5]
        l6=checkArray[2]&checkArray[4]&checkArray[6]
        l7=checkArray[6]&checkArray[7]&checkArray[8]
        l8=checkArray[2]&checkArray[5]&checkArray[8]
        if l1 or l2 or l3 or l4 or l5 or l6 or l7 or l8:
            self.fill_square(player1,square)

        if player1:
            squareMemory1[square-1] = checkArray
        else:
            squareMemory2[square-1] = checkArray

    def click_button(self, number):
        line = 'self.pushButton_' + str(number) + '.setEnabled(False)'
        eval(line)
        square = squareIndex[(number-1)]
        print(number)
        row = (number-1) // 9 % 3
        column = (number-1) % 3
        if self.turnCount % 2:
            color = "rgb(255,0,0)"
            self.check_for_complete(False, square, row, column)
        else:
            color = "rgb(255,192,203)"
            self.check_for_complete(True, square, row, column)

        line = 'self.pushButton_'+str(number)+'.setStyleSheet("background-color:'+color+'")'
        playsound('click.wav')
        eval(line)
        self.turnCount = self.turnCount+1

    def fill_square(self, player1, square):

        if player1:
            color = "rgb(255,192,203)"
            self.label.show()
            self.label_3.hide()
        else:
            color = "rgb(255,0,0)"
            self.label_3.show()
            self.label.hide()

        for ii in range(0,9):
            number = squareIndex2[square-1][ii]
            line = 'self.pushButton_' + str(number) + '.setStyleSheet("background-color:' + color + '")'
            eval(line)
            line = 'self.pushButton_' + str(number) + '.setEnabled(False)'
            eval(line)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


