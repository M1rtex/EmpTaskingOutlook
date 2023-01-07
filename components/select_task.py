# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_task.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 500)
        MainWindow.setMinimumSize(QSize(600, 500))
        MainWindow.setMaximumSize(QSize(600, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, -1, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tasks_listWidget = QListWidget(self.frame)
        self.tasks_listWidget.setObjectName(u"tasks_listWidget")
        self.tasks_listWidget.setGeometry(QRect(50, 40, 491, 271))
        self.tasks_listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tasks_listWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tasks_listWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tasks_listWidget.setMovement(QListView.Static)
        self.submit_btn = QPushButton(self.frame)
        self.submit_btn.setObjectName(u"submit_btn")
        self.submit_btn.setGeometry(QRect(150, 360, 281, 71))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QFont.PreferDefault)
        self.submit_btn.setFont(font)
        self.submit_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.submit_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
    # retranslateUi

