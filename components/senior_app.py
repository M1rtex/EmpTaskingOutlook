# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'senior_app.ui'
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
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1200, 600))
        font = QFont()
        font.setFamily(u"Segoe UI")
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setStyleSheet(u"")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tasks_main_frame = QFrame(self.main_frame)
        self.tasks_main_frame.setObjectName(u"tasks_main_frame")
        sizePolicy.setHeightForWidth(self.tasks_main_frame.sizePolicy().hasHeightForWidth())
        self.tasks_main_frame.setSizePolicy(sizePolicy)
        self.tasks_main_frame.setStyleSheet(u"#tasks_main_frame {\n"
                                            "	border: 0px;\n"
                                            "	border-right: 1px solid rgb(163, 163, 163);\n"
                                            "	border-bottom: 1px solid rgb(163, 163, 163);\n"
                                            "}")
        self.tasks_main_frame.setFrameShape(QFrame.StyledPanel)
        self.tasks_main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.tasks_main_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.selector_frame = QFrame(self.tasks_main_frame)
        self.selector_frame.setObjectName(u"selector_frame")
        self.selector_frame.setMaximumSize(QSize(16777215, 100))
        self.selector_frame.setStyleSheet(u"#selector_frame {\n"
                                          "	border: 0px;\n"
                                          "	border-bottom: 1px solid rgb(163, 163, 163);\n"
                                          "}\n"
                                          "\n"
                                          "\n"
                                          ".QPushButton {\n"
                                          "  background-color: rgb(255, 255, 255);\n"
                                          "  border: 2px solid #e7e7e7;\n"
                                          "  border-radius: 10px;\n"
                                          "}\n"
                                          "\n"
                                          ".QPushButton:hover {\n"
                                          "	background-color: #e7e7e7;\n"
                                          "}")
        self.selector_frame.setFrameShape(QFrame.StyledPanel)
        self.selector_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.selector_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.select_btns_frame = QFrame(self.selector_frame)
        self.select_btns_frame.setObjectName(u"select_btns_frame")
        self.select_btns_frame.setFrameShape(QFrame.StyledPanel)
        self.select_btns_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.select_btns_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.select_proj_btn = QPushButton(self.select_btns_frame)
        self.select_proj_btn.setObjectName(u"select_proj_btn")
        sizePolicy.setHeightForWidth(self.select_proj_btn.sizePolicy().hasHeightForWidth())
        self.select_proj_btn.setSizePolicy(sizePolicy)
        self.select_proj_btn.setMaximumSize(QSize(150, 40))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        self.select_proj_btn.setFont(font1)
        self.select_proj_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.select_proj_btn)

        self.select_staff_btn = QPushButton(self.select_btns_frame)
        self.select_staff_btn.setObjectName(u"select_staff_btn")
        sizePolicy.setHeightForWidth(self.select_staff_btn.sizePolicy().hasHeightForWidth())
        self.select_staff_btn.setSizePolicy(sizePolicy)
        self.select_staff_btn.setMaximumSize(QSize(150, 40))
        self.select_staff_btn.setFont(font1)
        self.select_staff_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.select_staff_btn)

        self.horizontalLayout_2.addWidget(self.select_btns_frame)

        self.frame_2 = QFrame(self.selector_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_4.addWidget(self.label)

        self.proj_lable = QLabel(self.frame_3)
        self.proj_lable.setObjectName(u"proj_lable")
        self.proj_lable.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.proj_lable)

        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_5.addWidget(self.label_7)

        self.staff_lable = QLabel(self.frame_4)
        self.staff_lable.setObjectName(u"staff_lable")
        self.staff_lable.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.staff_lable)

        self.verticalLayout_4.addWidget(self.frame_4)

        self.horizontalLayout_2.addWidget(self.frame_2)

        self.verticalLayout_2.addWidget(self.selector_frame)

        self.input_frame = QFrame(self.tasks_main_frame)
        self.input_frame.setObjectName(u"input_frame")
        self.input_frame.setStyleSheet(u"#input_frame {\n"
                                       "	border: 0px;\n"
                                       "	border-bottom: 1px solid rgb(163, 163, 163);\n"
                                       "}\n"
                                       "\n"
                                       ".QLineEdit {\n"
                                       "	border: 1px solid rgb(130, 130, 130);\n"
                                       "	border-radius: 6px;\n"
                                       "}")
        self.input_frame.setFrameShape(QFrame.StyledPanel)
        self.input_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.input_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.input_frame_S = QFrame(self.input_frame)
        self.input_frame_S.setObjectName(u"input_frame_S")
        self.input_frame_S.setFrameShape(QFrame.StyledPanel)
        self.input_frame_S.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.input_frame_S)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.input_frame_S)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(100, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.par_S_lable = QLabel(self.frame_6)
        self.par_S_lable.setObjectName(u"par_S_lable")
        self.par_S_lable.setMaximumSize(QSize(50, 50))
        self.par_S_lable.setStyleSheet(u"#par_S_lable {\n"
                                       "	border: 1px solid rgb(195, 195, 195);\n"
                                       "	border-radius: 10px;\n"
                                       "	background-color: rgb(195, 195, 195);\n"
                                       "}")
        self.par_S_lable.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.par_S_lable)

        self.horizontalLayout_6.addWidget(self.frame_6)

        self.frame_10 = QFrame(self.input_frame_S)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.par_S_lineedit = QLineEdit(self.frame_10)
        self.par_S_lineedit.setObjectName(u"par_S_lineedit")
        sizePolicy.setHeightForWidth(self.par_S_lineedit.sizePolicy().hasHeightForWidth())
        self.par_S_lineedit.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(10)
        self.par_S_lineedit.setFont(font2)

        self.horizontalLayout_7.addWidget(self.par_S_lineedit)

        self.horizontalLayout_6.addWidget(self.frame_10)

        self.verticalLayout_5.addWidget(self.input_frame_S)

        self.input_frame_M = QFrame(self.input_frame)
        self.input_frame_M.setObjectName(u"input_frame_M")
        self.input_frame_M.setFrameShape(QFrame.StyledPanel)
        self.input_frame_M.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.input_frame_M)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.input_frame_M)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(100, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.par_M_lable = QLabel(self.frame_8)
        self.par_M_lable.setObjectName(u"par_M_lable")
        self.par_M_lable.setMaximumSize(QSize(50, 50))
        self.par_M_lable.setStyleSheet(u"#par_M_lable {\n"
                                       "	border: 1px solid rgb(195, 195, 195);\n"
                                       "	border-radius: 10px;\n"
                                       "	background-color: rgb(195, 195, 195);\n"
                                       "}")
        self.par_M_lable.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.par_M_lable)

        self.horizontalLayout_11.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.input_frame_M)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.par_M_lineedit = QLineEdit(self.frame_9)
        self.par_M_lineedit.setObjectName(u"par_M_lineedit")
        sizePolicy.setHeightForWidth(self.par_M_lineedit.sizePolicy().hasHeightForWidth())
        self.par_M_lineedit.setSizePolicy(sizePolicy)
        self.par_M_lineedit.setFont(font2)

        self.horizontalLayout_10.addWidget(self.par_M_lineedit)

        self.horizontalLayout_11.addWidget(self.frame_9)

        self.verticalLayout_5.addWidget(self.input_frame_M)

        self.input_frame_A = QFrame(self.input_frame)
        self.input_frame_A.setObjectName(u"input_frame_A")
        self.input_frame_A.setFrameShape(QFrame.StyledPanel)
        self.input_frame_A.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.input_frame_A)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.input_frame_A)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(100, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.par_A_lable = QLabel(self.frame_12)
        self.par_A_lable.setObjectName(u"par_A_lable")
        self.par_A_lable.setMaximumSize(QSize(50, 50))
        self.par_A_lable.setStyleSheet(u"#par_A_lable {\n"
                                       "	border: 1px solid rgb(195, 195, 195);\n"
                                       "	border-radius: 10px;\n"
                                       "	background-color: rgb(195, 195, 195);\n"
                                       "}")
        self.par_A_lable.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.par_A_lable)

        self.horizontalLayout_14.addWidget(self.frame_12)

        self.frame_11 = QFrame(self.input_frame_A)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.par_A_lineedit = QLineEdit(self.frame_11)
        self.par_A_lineedit.setObjectName(u"par_A_lineedit")
        sizePolicy.setHeightForWidth(self.par_A_lineedit.sizePolicy().hasHeightForWidth())
        self.par_A_lineedit.setSizePolicy(sizePolicy)
        self.par_A_lineedit.setFont(font2)

        self.horizontalLayout_12.addWidget(self.par_A_lineedit)

        self.horizontalLayout_14.addWidget(self.frame_11)

        self.verticalLayout_5.addWidget(self.input_frame_A)

        self.input_frame_R = QFrame(self.input_frame)
        self.input_frame_R.setObjectName(u"input_frame_R")
        self.input_frame_R.setFrameShape(QFrame.StyledPanel)
        self.input_frame_R.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.input_frame_R)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.input_frame_R)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(100, 16777215))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.par_R_lable = QLabel(self.frame_13)
        self.par_R_lable.setObjectName(u"par_R_lable")
        self.par_R_lable.setMaximumSize(QSize(50, 50))
        self.par_R_lable.setStyleSheet(u"#par_R_lable {\n"
                                       "	border: 1px solid rgb(195, 195, 195);\n"
                                       "	border-radius: 10px;\n"
                                       "	background-color: rgb(195, 195, 195);\n"
                                       "}")
        self.par_R_lable.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.par_R_lable)

        self.horizontalLayout_18.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.input_frame_R)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.par_R_lineedit = QLineEdit(self.frame_14)
        self.par_R_lineedit.setObjectName(u"par_R_lineedit")
        sizePolicy.setHeightForWidth(self.par_R_lineedit.sizePolicy().hasHeightForWidth())
        self.par_R_lineedit.setSizePolicy(sizePolicy)
        self.par_R_lineedit.setFont(font2)

        self.horizontalLayout_17.addWidget(self.par_R_lineedit)

        self.horizontalLayout_18.addWidget(self.frame_14)

        self.verticalLayout_5.addWidget(self.input_frame_R)

        self.input_frame_T = QFrame(self.input_frame)
        self.input_frame_T.setObjectName(u"input_frame_T")
        self.input_frame_T.setFrameShape(QFrame.StyledPanel)
        self.input_frame_T.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.input_frame_T)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.input_frame_T)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(100, 16777215))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.par_T_lable = QLabel(self.frame_15)
        self.par_T_lable.setObjectName(u"par_T_lable")
        self.par_T_lable.setMaximumSize(QSize(50, 50))
        self.par_T_lable.setStyleSheet(u"#par_T_lable {\n"
                                       "	border: 1px solid rgb(195, 195, 195);\n"
                                       "	border-radius: 10px;\n"
                                       "	background-color: rgb(195, 195, 195);\n"
                                       "}")
        self.par_T_lable.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.par_T_lable)

        self.horizontalLayout_21.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.input_frame_T)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.par_T_lineedit = QLineEdit(self.frame_16)
        self.par_T_lineedit.setObjectName(u"par_T_lineedit")
        sizePolicy.setHeightForWidth(self.par_T_lineedit.sizePolicy().hasHeightForWidth())
        self.par_T_lineedit.setSizePolicy(sizePolicy)
        self.par_T_lineedit.setFont(font2)

        self.horizontalLayout_20.addWidget(self.par_T_lineedit)

        self.horizontalLayout_21.addWidget(self.frame_16)

        self.verticalLayout_5.addWidget(self.input_frame_T)

        self.verticalLayout_2.addWidget(self.input_frame)

        self.tasks_btns_frame = QFrame(self.tasks_main_frame)
        self.tasks_btns_frame.setObjectName(u"tasks_btns_frame")
        self.tasks_btns_frame.setMaximumSize(QSize(16777215, 120))
        self.tasks_btns_frame.setStyleSheet(u"\n"
                                            ".QPushButton {\n"
                                            "  background-color: rgb(255, 255, 255);\n"
                                            "  border: 2px solid #e7e7e7;\n"
                                            "  border-radius: 10px;\n"
                                            "}\n"
                                            "\n"
                                            ".QPushButton:hover {\n"
                                            "	background-color: #e7e7e7;\n"
                                            "}")
        self.tasks_btns_frame.setFrameShape(QFrame.StyledPanel)
        self.tasks_btns_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.tasks_btns_frame)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame = QFrame(self.tasks_btns_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(100, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.settings_btn = QPushButton(self.frame)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setMaximumSize(QSize(50, 50))
        self.settings_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/settings.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_btn.setIcon(icon)
        self.settings_btn.setIconSize(QSize(16, 16))

        self.horizontalLayout_25.addWidget(self.settings_btn)

        self.horizontalLayout_22.addWidget(self.frame)

        self.frame_7 = QFrame(self.tasks_btns_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setLayoutDirection(Qt.LeftToRight)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.cancel_btn = QPushButton(self.frame_7)
        self.cancel_btn.setObjectName(u"cancel_btn")
        sizePolicy.setHeightForWidth(self.cancel_btn.sizePolicy().hasHeightForWidth())
        self.cancel_btn.setSizePolicy(sizePolicy)
        self.cancel_btn.setMinimumSize(QSize(0, 0))
        self.cancel_btn.setMaximumSize(QSize(180, 60))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        self.cancel_btn.setFont(font3)
        self.cancel_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_23.addWidget(self.cancel_btn)

        self.horizontalLayout_22.addWidget(self.frame_7)

        self.frame_5 = QFrame(self.tasks_btns_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_22 = QFrame(self.frame_5)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_15.addWidget(self.frame_22)

        self.submit_task_icon = QLabel(self.frame_5)
        self.submit_task_icon.setObjectName(u"submit_task_icon")
        self.submit_task_icon.setEnabled(True)
        self.submit_task_icon.setMaximumSize(QSize(70, 40))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setWeight(50)
        self.submit_task_icon.setFont(font4)
        self.submit_task_icon.setTextFormat(Qt.AutoText)
        self.submit_task_icon.setScaledContents(True)
        self.submit_task_icon.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.submit_task_icon.setTextInteractionFlags(Qt.LinksAccessibleByMouse)

        self.horizontalLayout_15.addWidget(self.submit_task_icon)

        self.horizontalLayout_22.addWidget(self.frame_5)

        self.frame_17 = QFrame(self.tasks_btns_frame)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.submit_task_btn = QPushButton(self.frame_17)
        self.submit_task_btn.setObjectName(u"submit_task_btn")
        sizePolicy.setHeightForWidth(self.submit_task_btn.sizePolicy().hasHeightForWidth())
        self.submit_task_btn.setSizePolicy(sizePolicy)
        self.submit_task_btn.setMinimumSize(QSize(0, 0))
        self.submit_task_btn.setMaximumSize(QSize(180, 60))
        self.submit_task_btn.setFont(font3)
        self.submit_task_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.submit_task_btn.setCheckable(False)

        self.horizontalLayout_24.addWidget(self.submit_task_btn)

        self.horizontalLayout_22.addWidget(self.frame_17)

        self.verticalLayout_2.addWidget(self.tasks_btns_frame)

        self.horizontalLayout.addWidget(self.tasks_main_frame)

        self.shedule_main_frame = QFrame(self.main_frame)
        self.shedule_main_frame.setObjectName(u"shedule_main_frame")
        self.shedule_main_frame.setMaximumSize(QSize(300, 16777215))
        self.shedule_main_frame.setStyleSheet(u"#shedule_main_frame {\n"
                                              "	border: 0px;\n"
                                              "	border-bottom: 1px solid rgb(163, 163, 163);\n"
                                              "}")
        self.shedule_main_frame.setFrameShape(QFrame.StyledPanel)
        self.shedule_main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.shedule_main_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lable_frame = QFrame(self.shedule_main_frame)
        self.lable_frame.setObjectName(u"lable_frame")
        self.lable_frame.setMaximumSize(QSize(16777215, 100))
        self.lable_frame.setFrameShape(QFrame.StyledPanel)
        self.lable_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.lable_frame)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(-1, 0, 0, 0)
        self.frame_23 = QFrame(self.lable_frame)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_23)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.kalendar_lable = QLabel(self.frame_23)
        self.kalendar_lable.setObjectName(u"kalendar_lable")
        self.kalendar_lable.setStyleSheet(u"#kalendar_lable {\n"
                                          "	background-color: #c8c8c8;\n"
                                          "	border: 2px solid #c8c8c8;\n"
                                          "	border-radius: 20px;\n"
                                          "}")
        self.kalendar_lable.setTextFormat(Qt.AutoText)

        self.verticalLayout_9.addWidget(self.kalendar_lable)

        self.task_selector_frame = QFrame(self.frame_23)
        self.task_selector_frame.setObjectName(u"task_selector_frame")
        self.task_selector_frame.setStyleSheet(u".QPushButton {\n"
                                               "  background-color: rgb(255, 255, 255);\n"
                                               "  border: 2px solid #e7e7e7;\n"
                                               "  border-radius: 10px;\n"
                                               "}\n"
                                               "\n"
                                               ".QPushButton:hover {\n"
                                               "	background-color: #e7e7e7;\n"
                                               "}")
        self.task_selector_frame.setFrameShape(QFrame.StyledPanel)
        self.task_selector_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.task_selector_frame)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.select_task_btn = QPushButton(self.task_selector_frame)
        self.select_task_btn.setObjectName(u"select_task_btn")
        self.select_task_btn.setEnabled(True)
        sizePolicy.setHeightForWidth(self.select_task_btn.sizePolicy().hasHeightForWidth())
        self.select_task_btn.setSizePolicy(sizePolicy)
        self.select_task_btn.setFont(font1)

        self.horizontalLayout_29.addWidget(self.select_task_btn)

        self.selected_task_frame = QFrame(self.task_selector_frame)
        self.selected_task_frame.setObjectName(u"selected_task_frame")
        self.selected_task_frame.setFrameShape(QFrame.StyledPanel)
        self.selected_task_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.selected_task_frame)
        self.horizontalLayout_30.setSpacing(5)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.selected_task_frame)
        self.label_4.setObjectName(u"label_4")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_4.setFont(font5)
        self.label_4.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.label_4)

        self.task_num_lable = QLabel(self.selected_task_frame)
        self.task_num_lable.setObjectName(u"task_num_lable")
        self.task_num_lable.setFont(font3)

        self.horizontalLayout_30.addWidget(self.task_num_lable)

        self.horizontalLayout_29.addWidget(self.selected_task_frame)

        self.verticalLayout_9.addWidget(self.task_selector_frame)

        self.horizontalLayout_26.addWidget(self.frame_23)

        self.verticalLayout_3.addWidget(self.lable_frame)

        self.datetime_frame = QFrame(self.shedule_main_frame)
        self.datetime_frame.setObjectName(u"datetime_frame")
        self.datetime_frame.setStyleSheet(u"")
        self.datetime_frame.setFrameShape(QFrame.StyledPanel)
        self.datetime_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.datetime_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_18 = QFrame(self.datetime_frame)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_18)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.frame_18)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_8.addWidget(self.label_3)

        self.start_dateEdit = QDateEdit(self.frame_18)
        self.start_dateEdit.setObjectName(u"start_dateEdit")
        self.start_dateEdit.setProperty("showGroupSeparator", False)
        self.start_dateEdit.setDateTime(QDateTime(QDate(2022, 12, 31), QTime(18, 0, 0)))
        self.start_dateEdit.setMinimumDate(QDate(2022, 12, 27))
        self.start_dateEdit.setCalendarPopup(True)
        self.start_dateEdit.setTimeSpec(Qt.OffsetFromUTC)

        self.verticalLayout_8.addWidget(self.start_dateEdit)

        self.verticalLayout_6.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.datetime_frame)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_19)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.frame_19)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_7.addWidget(self.label_2)

        self.end_dateEdit = QDateEdit(self.frame_19)
        self.end_dateEdit.setObjectName(u"end_dateEdit")
        self.end_dateEdit.setDateTime(QDateTime(QDate(2023, 1, 2), QTime(18, 0, 0)))
        self.end_dateEdit.setMinimumDate(QDate(2022, 12, 28))
        self.end_dateEdit.setCalendarPopup(True)
        self.end_dateEdit.setTimeSpec(Qt.OffsetFromUTC)
        self.end_dateEdit.setDate(QDate(2023, 1, 2))

        self.verticalLayout_7.addWidget(self.end_dateEdit)

        self.verticalLayout_6.addWidget(self.frame_19)

        self.verticalLayout_3.addWidget(self.datetime_frame)

        self.shedule_btns_frame = QFrame(self.shedule_main_frame)
        self.shedule_btns_frame.setObjectName(u"shedule_btns_frame")
        self.shedule_btns_frame.setStyleSheet(u"\n"
                                              ".QPushButton {\n"
                                              "  background-color: rgb(255, 255, 255);\n"
                                              "  border: 2px solid #e7e7e7;\n"
                                              "  border-radius: 10px;\n"
                                              "}\n"
                                              "\n"
                                              ".QPushButton:hover {\n"
                                              "	background-color: #e7e7e7;\n"
                                              "}")
        self.shedule_btns_frame.setFrameShape(QFrame.StyledPanel)
        self.shedule_btns_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.shedule_btns_frame)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.shedule_btns_frame)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 0))
        self.frame_20.setMaximumSize(QSize(200, 200))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_20)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.cancel_datetime = QPushButton(self.frame_20)
        self.cancel_datetime.setObjectName(u"cancel_datetime")
        sizePolicy.setHeightForWidth(self.cancel_datetime.sizePolicy().hasHeightForWidth())
        self.cancel_datetime.setSizePolicy(sizePolicy)
        self.cancel_datetime.setMaximumSize(QSize(180, 40))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(11)
        self.cancel_datetime.setFont(font6)
        self.cancel_datetime.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_10.addWidget(self.cancel_datetime)

        self.submit_datetime_btn = QPushButton(self.frame_20)
        self.submit_datetime_btn.setObjectName(u"submit_datetime_btn")
        sizePolicy.setHeightForWidth(self.submit_datetime_btn.sizePolicy().hasHeightForWidth())
        self.submit_datetime_btn.setSizePolicy(sizePolicy)
        self.submit_datetime_btn.setMaximumSize(QSize(180, 60))
        self.submit_datetime_btn.setFont(font3)
        self.submit_datetime_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_10.addWidget(self.submit_datetime_btn)

        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setEnabled(True)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(-1, 0, -1, -1)
        self.submit_datetime_icon = QLabel(self.frame_21)
        self.submit_datetime_icon.setObjectName(u"submit_datetime_icon")
        self.submit_datetime_icon.setEnabled(True)
        self.submit_datetime_icon.setMaximumSize(QSize(80, 40))
        self.submit_datetime_icon.setFont(font6)
        self.submit_datetime_icon.setScaledContents(True)

        self.horizontalLayout_28.addWidget(self.submit_datetime_icon)

        self.verticalLayout_10.addWidget(self.frame_21)

        self.horizontalLayout_27.addWidget(self.frame_20)

        self.verticalLayout_3.addWidget(self.shedule_btns_frame)

        self.horizontalLayout.addWidget(self.shedule_main_frame)

        self.verticalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.select_proj_btn.setText(
            QCoreApplication.translate("MainWindow", u"\u0432\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0440\u043e\u0435\u043a\u0442",
                                       None))
        self.select_staff_btn.setText(QCoreApplication.translate("MainWindow",
                                                                 u"\u0432\u044b\u0431\u0440\u0430\u0442\u044c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0430",
                                                                 None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">\u041f\u0440\u043e\u0435\u043a\u0442:</span></p></body></html>",
                                                      None))
        self.proj_lable.setText(QCoreApplication.translate("MainWindow",
                                                           u"<html><head/><body><p><span style=\" font-size:10pt;\">\u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d\u043e</span></p></body></html>",
                                                           None))
        self.label_7.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a:</span></p></body></html>",
                                                        None))
        self.staff_lable.setText(QCoreApplication.translate("MainWindow",
                                                            u"<html><head/><body><p><span style=\" font-size:10pt;\">\u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d\u043e</span></p></body></html>",
                                                            None))
        self.par_S_lable.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.par_S_lineedit.setInputMask("")
        self.par_S_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                          u"\u043a\u043e\u043d\u0442\u0435\u043d\u0442 \u043f\u0430\u0440\u0430\u043c\u0435\u0440\u0442\u0440\u0430 S",
                                                                          None))
        self.par_M_lable.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.par_M_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                          u"\u043a\u043e\u043d\u0442\u0435\u043d\u0442 \u043f\u0430\u0440\u0430\u043c\u0435\u0440\u0442\u0440\u0430 M",
                                                                          None))
        self.par_A_lable.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.par_A_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                          u"\u043a\u043e\u043d\u0442\u0435\u043d\u0442 \u043f\u0430\u0440\u0430\u043c\u0435\u0440\u0442\u0440\u0430 A",
                                                                          None))
        self.par_R_lable.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.par_R_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                          u"\u043a\u043e\u043d\u0442\u0435\u043d\u0442 \u043f\u0430\u0440\u0430\u043c\u0435\u0440\u0442\u0440\u0430 R",
                                                                          None))
        self.par_T_lable.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.par_T_lineedit.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                          u"\u043a\u043e\u043d\u0442\u0435\u043d\u0442 \u043f\u0430\u0440\u0430\u043c\u0435\u0440\u0442\u0440\u0430 T",
                                                                          None))
        self.settings_btn.setText("")
        self.cancel_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.submit_task_icon.setText(
            QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430", None))
        self.submit_task_btn.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443",
                                                                None))
        self.kalendar_lable.setText(QCoreApplication.translate("MainWindow",
                                                               u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">\u041a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044c</span></p></body></html>",
                                                               None))
        self.select_task_btn.setText(
            QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443",
                                       None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0447\u0430", None))
        self.task_num_lable.setText(QCoreApplication.translate("MainWindow", u"\u043d\u043e\u043c\u0435\u0440", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">\u041d\u0430\u0447\u0438\u043d\u0430\u044f \u0441</span></p></body></html>",
                                                        None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">\u0414\u043e</span></p></body></html>",
                                                        None))
        self.cancel_datetime.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.submit_datetime_btn.setText(QCoreApplication.translate("MainWindow",
                                                                    u"\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u0440\u043e\u043a",
                                                                    None))
        self.submit_datetime_icon.setText(
            QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430", None))
    # retranslateUi
