# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_selectdate.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QDateEdit, QHBoxLayout,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_SelectDate(object):
    def setupUi(self, SelectDate):
        if not SelectDate.objectName():
            SelectDate.setObjectName(u"SelectDate")
        SelectDate.resize(391, 300)
        SelectDate.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #1b1b27;\n"
"}\n"
"QDateEdit, QPushButton{\n"
"	padding: 5px 10px;\n"
"	border-radius: 10px;\n"
"	background-color: #27263c;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(SelectDate)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.centralwidget = QWidget(SelectDate)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.cld_widget = QCalendarWidget(self.centralwidget)
        self.cld_widget.setObjectName(u"cld_widget")
        self.cld_widget.setStyleSheet(u"QCalendarWidget QToolButton{\n"
"	background-color : #27263c;\n"
"}\n"
"QCalendarWidget QToolButton::hover{\n"
"	background-color : cyan;\n"
"}\n"
"QCalendarWidget QToolButton::pressed{\n"
"	background-color : red;\n"
"}\n"
"\n"
"QCalendarWidget QWidget { alternate-background-color: rgb(128, 128, 128); }\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled \n"
"  {\n"
"  	font-size:14px;  \n"
"  	color: white;\n"
"  	background-color: black;  \n"
"  	selection-background-color: rgb(64, 64, 64); \n"
"  	selection-color: rgb(0, 255, 0); \n"
"  }\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar\n"
"{ \n"
"  background-color: #27263c; \n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:disabled \n"
"{ \n"
"	color: rgb(64, 64, 64); \n"
"}")

        self.verticalLayout_2.addWidget(self.cld_widget)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.date_select = QDateEdit(self.widget)
        self.date_select.setObjectName(u"date_select")

        self.horizontalLayout.addWidget(self.date_select)

        self.bnt_savedate = QPushButton(self.widget)
        self.bnt_savedate.setObjectName(u"bnt_savedate")

        self.horizontalLayout.addWidget(self.bnt_savedate)


        self.verticalLayout_2.addWidget(self.widget)


        self.verticalLayout.addWidget(self.centralwidget)


        self.retranslateUi(SelectDate)

        QMetaObject.connectSlotsByName(SelectDate)
    # setupUi

    def retranslateUi(self, SelectDate):
        SelectDate.setWindowTitle(QCoreApplication.translate("SelectDate", u"Seleccionar fecha", None))
        self.bnt_savedate.setText(QCoreApplication.translate("SelectDate", u"Ok", None))
    # retranslateUi

