# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_budgetdata.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_BudgetData(object):
    def setupUi(self, BudgetData):
        if not BudgetData.objectName():
            BudgetData.setObjectName(u"BudgetData")
        BudgetData.resize(700, 650)
        BudgetData.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color: #1b1b27;\n"
"}\n"
"QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"QLineEdit, QDateEdit, QComboBox, #btn_date{\n"
"	padding: 5px 10px;\n"
"	border-radius: 10px;\n"
"	background-color: #27263c;\n"
"}\n"
"\n"
"#btn_newrow {\n"
"	border: 2px solid  #ece424 ;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
" #btn_newrow  {\n"
"	border: 2px solid  #ece424 ;\n"
"	background-color: #9c991c ;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
" #btn_newrow:pressed   {\n"
"	background-color: #9C995F ;\n"
"}")
        self.verticalLayout = QVBoxLayout(BudgetData)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.centralwidget = QWidget(BudgetData)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 30)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 30, -1)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.budget_number = QLabel(self.frame)
        self.budget_number.setObjectName(u"budget_number")
        self.budget_number.setFont(font)

        self.horizontalLayout.addWidget(self.budget_number, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignHCenter)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.frame_2.setFont(font1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_2, 0, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.btn_newrow = QPushButton(self.widget)
        self.btn_newrow.setObjectName(u"btn_newrow")

        self.verticalLayout_3.addWidget(self.btn_newrow, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.type_combobox = QComboBox(self.widget_2)
        self.type_combobox.setObjectName(u"type_combobox")

        self.horizontalLayout_2.addWidget(self.type_combobox)

        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.widget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.widget_2, 0, Qt.AlignTop)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_5.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label_5, 0, Qt.AlignRight)

        self.iva_combobox = QComboBox(self.widget_3)
        self.iva_combobox.setObjectName(u"iva_combobox")

        self.horizontalLayout_4.addWidget(self.iva_combobox)

        self.lineEdit_3 = QLineEdit(self.widget_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_4.addWidget(self.lineEdit_3, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.widget_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.centralwidget)


        self.retranslateUi(BudgetData)

        QMetaObject.connectSlotsByName(BudgetData)
    # setupUi

    def retranslateUi(self, BudgetData):
        BudgetData.setWindowTitle(QCoreApplication.translate("BudgetData", u"Nuevo Presupuesto", None))
        self.label_3.setText(QCoreApplication.translate("BudgetData", u"Presupuesto N\u00b0", None))
        self.budget_number.setText(QCoreApplication.translate("BudgetData", u"#", None))
        self.label.setText(QCoreApplication.translate("BudgetData", u"Descripci\u00f3n", None))
        self.label_2.setText(QCoreApplication.translate("BudgetData", u"Precio", None))
        self.btn_newrow.setText(QCoreApplication.translate("BudgetData", u"A\u00f1adir fila", None))
        self.label_4.setText(QCoreApplication.translate("BudgetData", u"Precio Total", None))
        self.label_5.setText(QCoreApplication.translate("BudgetData", u"IVA", None))
    # retranslateUi

