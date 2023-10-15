# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appNULTHD.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(409, 189)
        font = QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.widget = QWidget(MainWindow)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(8, -1, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_ip = QLineEdit(self.widget)
        self.lineEdit_ip.setObjectName(u"lineEdit_ip")
        self.lineEdit_ip.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lineEdit_ip)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_port = QLineEdit(self.widget)
        self.lineEdit_port.setObjectName(u"lineEdit_port")
        self.lineEdit_port.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lineEdit_port)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_connect = QPushButton(self.widget)
        self.pushButton_connect.setObjectName(u"pushButton_connect")
        self.pushButton_connect.setMinimumSize(QSize(60, 30))
        self.pushButton_connect.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButton_connect)

        self.pushButton_DisCon = QPushButton(self.widget)
        self.pushButton_DisCon.setObjectName(u"pushButton_DisCon")
        self.pushButton_DisCon.setMinimumSize(QSize(60, 30))
        self.pushButton_DisCon.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pushButton_DisCon)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(4, -1, -1, -1)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.lineEdit_Rdata = QLineEdit(self.widget)
        self.lineEdit_Rdata.setObjectName(u"lineEdit_Rdata")
        self.lineEdit_Rdata.setMaxLength(8)
        self.lineEdit_Rdata.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lineEdit_Rdata)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.label_keyStroke = QLabel(self.widget)
        self.label_keyStroke.setObjectName(u"label_keyStroke")

        self.horizontalLayout_5.addWidget(self.label_keyStroke)

        self.pushButton_keySet = QPushButton(self.widget)
        self.pushButton_keySet.setObjectName(u"pushButton_keySet")
        self.pushButton_keySet.setMinimumSize(QSize(45, 30))
        self.pushButton_keySet.setMaximumSize(QSize(50, 35))

        self.horizontalLayout_5.addWidget(self.pushButton_keySet)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.line_3 = QFrame(self.widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        MainWindow.setCentralWidget(self.widget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 409, 31))
        self.menuabout = QMenu(self.menubar)
        self.menuabout.setObjectName(u"menuabout")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menuabout.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TCP key controller", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"IP Address", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.pushButton_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.pushButton_DisCon.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"received data", None))
        self.lineEdit_Rdata.setText(QCoreApplication.translate("MainWindow", u"data", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"keystroke :- ", None))
        self.label_keyStroke.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_keySet.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuabout.setTitle(QCoreApplication.translate("MainWindow", u"about", None))
    # retranslateUi

