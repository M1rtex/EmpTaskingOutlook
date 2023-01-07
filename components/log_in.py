# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log_in.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from components import icons


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(475, 380)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(475, 380))
        MainWindow.setMaximumSize(QSize(475, 380))
        font = QFont()
        font.setFamily(u"Segoe UI")
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.text_frame = QFrame(self.main_frame)
        self.text_frame.setObjectName(u"text_frame")
        self.text_frame.setFrameShape(QFrame.StyledPanel)
        self.text_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.text_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.info_text_frame = QFrame(self.text_frame)
        self.info_text_frame.setObjectName(u"info_text_frame")
        self.info_text_frame.setMinimumSize(QSize(0, 70))
        self.info_text_frame.setFrameShape(QFrame.StyledPanel)
        self.info_text_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.info_text_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.info_text_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.label_2)

        self.verticalLayout_2.addWidget(self.info_text_frame)

        self.help_text_frame = QFrame(self.text_frame)
        self.help_text_frame.setObjectName(u"help_text_frame")
        self.help_text_frame.setFrameShape(QFrame.StyledPanel)
        self.help_text_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.help_text_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.help_text_frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label)

        self.verticalLayout_2.addWidget(self.help_text_frame)

        self.verticalLayout.addWidget(self.text_frame)

        self.code_frame = QFrame(self.main_frame)
        self.code_frame.setObjectName(u"code_frame")
        self.code_frame.setMaximumSize(QSize(16777215, 80))
        self.code_frame.setFrameShape(QFrame.StyledPanel)
        self.code_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.code_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 5, 0, 5)
        self.code_text_frame = QFrame(self.code_frame)
        self.code_text_frame.setObjectName(u"code_text_frame")
        self.code_text_frame.setMaximumSize(QSize(350, 16777215))
        self.code_text_frame.setStyleSheet(u"#code_text_frame {\n"
                                           "  background-color: rgb(255, 255, 255);\n"
                                           "  border-radius: 25px;\n"
                                           "}\n"
                                           "")
        self.code_text_frame.setFrameShape(QFrame.StyledPanel)
        self.code_text_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.code_text_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.login_code_lable = QLabel(self.code_text_frame)
        self.login_code_lable.setObjectName(u"login_code_lable")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(35)
        self.login_code_lable.setFont(font1)
        self.login_code_lable.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.login_code_lable)

        self.horizontalLayout_5.addWidget(self.code_text_frame)

        self.verticalLayout.addWidget(self.code_frame)

        self.butons_frame = QFrame(self.main_frame)
        self.butons_frame.setObjectName(u"butons_frame")
        self.butons_frame.setMinimumSize(QSize(0, 0))
        self.butons_frame.setFrameShape(QFrame.StyledPanel)
        self.butons_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.butons_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.butons_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u".QPushButton {\n"
                                 "  background-color: rgb(255, 255, 255);\n"
                                 "  border: 2px solid #e7e7e7;\n"
                                 "  border-radius: 10px;\n"
                                 "}\n"
                                 "\n"
                                 ".QPushButton:hover {\n"
                                 "	background-color: #e7e7e7;\n"
                                 "}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.copy_login_code_btn = QPushButton(self.frame)
        self.copy_login_code_btn.setObjectName(u"copy_login_code_btn")
        sizePolicy.setHeightForWidth(self.copy_login_code_btn.sizePolicy().hasHeightForWidth())
        self.copy_login_code_btn.setSizePolicy(sizePolicy)
        self.copy_login_code_btn.setMaximumSize(QSize(250, 55))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(15)
        font2.setBold(False)
        font2.setWeight(50)
        self.copy_login_code_btn.setFont(font2)
        self.copy_login_code_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.copy_login_code_btn)

        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.butons_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 32))
        self.frame_2.setStyleSheet(u".QPushButton {\n"
                                   "  background-color: rgb(255, 255, 255);\n"
                                   "  border: 2px solid #e7e7e7;\n"
                                   "  border-radius: 10;\n"
                                   "}\n"
                                   "\n"
                                   ".QPushButton:hover {\n"
                                   "	background-color: #e7e7e7;\n"
                                   "}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(32, 32))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon = QIcon()
        icon.addFile(u":/icons/settings.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.horizontalLayout_2.addWidget(self.frame_4)

        self.verticalLayout_3.addWidget(self.frame_2)

        self.verticalLayout.addWidget(self.butons_frame)

        self.horizontalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">\u042d\u0442\u043e </span><span style=\" font-size:14pt; font-weight:600;\">\u043e\u043a\u043d\u043e \u0430\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u0438.</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">\u041f\u0435\u0440\u0435\u0439\u0434\u0438\u0442\u0435</span><span style=\" font-size:12pt;\"> \u043d\u0430 </span><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">https://microsoft.com/devicelogin</span><span style=\" font-size:12pt;\">, </span><span style=\" font-size:12pt; font-weight:600;\">\u0432\u0432\u0435\u0434\u0438\u0442\u0435</span><span style=\" font-size:12pt;\"> \u043a\u043e\u0434, \u0438 </span><span style=\" font-size:12pt; font-weight:600;\">\u0430\u0432\u0442\u043e\u0440\u0438\u0437\u0443\u0451\u0442\u0435\u0441\u044c</span><span style=\" font-size:12pt;\"> \u0432 \u0443\u0447. \u0437\u0430\u043f\u0438\u0441\u0438.</span></p></body></html>",
                                                        None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">\u0412\u0430\u0448 \u043a\u043e\u0434:</span></p></body></html>",
                                                      None))
        self.login_code_lable.setText("")
        self.copy_login_code_btn.setText(QCoreApplication.translate("MainWindow",
                                                                    u"\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c",
                                                                    None))
        self.pushButton_2.setText("")
    # retranslateUi
