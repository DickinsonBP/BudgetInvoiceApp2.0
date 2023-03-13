# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_edituser.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_EditUserWindow(object):
    def setupUi(self, EditUserWindow):
        if not EditUserWindow.objectName():
            EditUserWindow.setObjectName(u"EditUserWindow")
        EditUserWindow.resize(700, 650)
        EditUserWindow.setStyleSheet(u"*{\n"
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
"QLineEdit{\n"
"	padding: 5px 10px;\n"
"	border-radius: 10px;\n"
"	background-color: #27263c;\n"
"}\n"
"\n"
"#btn_saveuser, #btn_cancel  {\n"
"	border: 2px solid  #ece424 ;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
" #btn_saveuser, #btn_cancel   {\n"
"	border: 2px solid  #ece424 ;\n"
"	background-color: #9c991c ;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
" #btn_saveuser:pressed, #btn_cancel:pressed   {\n"
"	background-color: #9C995F ;\n"
"}")
        self.verticalLayout = QVBoxLayout(EditUserWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.centralwidget = QWidget(EditUserWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.frame)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_nif = QLabel(self.widget_2)
        self.label_nif.setObjectName(u"label_nif")
        font1 = QFont()
        font1.setBold(True)
        self.label_nif.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_nif)

        self.line_nif = QLineEdit(self.widget_2)
        self.line_nif.setObjectName(u"line_nif")

        self.verticalLayout_4.addWidget(self.line_nif)

        self.label_name = QLabel(self.widget_2)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_name)

        self.line_name = QLineEdit(self.widget_2)
        self.line_name.setObjectName(u"line_name")

        self.verticalLayout_4.addWidget(self.line_name)

        self.label_email = QLabel(self.widget_2)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_email)

        self.line_email = QLineEdit(self.widget_2)
        self.line_email.setObjectName(u"line_email")

        self.verticalLayout_4.addWidget(self.line_email)

        self.label_phone = QLabel(self.widget_2)
        self.label_phone.setObjectName(u"label_phone")
        self.label_phone.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_phone)

        self.line_phone = QLineEdit(self.widget_2)
        self.line_phone.setObjectName(u"line_phone")

        self.verticalLayout_4.addWidget(self.line_phone)

        self.label_address = QLabel(self.widget_2)
        self.label_address.setObjectName(u"label_address")
        self.label_address.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_address)

        self.line_address = QLineEdit(self.widget_2)
        self.line_address.setObjectName(u"line_address")

        self.verticalLayout_4.addWidget(self.line_address)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_saveuser = QPushButton(self.widget_3)
        self.btn_saveuser.setObjectName(u"btn_saveuser")
        self.btn_saveuser.setFont(font1)
        self.btn_saveuser.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"../res/Icons/check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_saveuser.setIcon(icon)
        self.btn_saveuser.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_saveuser, 0, Qt.AlignHCenter)

        self.btn_cancel = QPushButton(self.widget_3)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setFont(font1)
        self.btn_cancel.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"../res/Icons/thumbs-down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cancel.setIcon(icon1)
        self.btn_cancel.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_cancel, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.widget_3)


        self.verticalLayout_3.addWidget(self.widget_2)


        self.verticalLayout_2.addWidget(self.widget)


        self.verticalLayout.addWidget(self.centralwidget)


        self.retranslateUi(EditUserWindow)

        QMetaObject.connectSlotsByName(EditUserWindow)
    # setupUi

    def retranslateUi(self, EditUserWindow):
        EditUserWindow.setWindowTitle(QCoreApplication.translate("EditUserWindow", u"Editar Usuario", None))
        self.label.setText(QCoreApplication.translate("EditUserWindow", u"Editar Usuario", None))
        self.label_nif.setText(QCoreApplication.translate("EditUserWindow", u"NIF", None))
        self.label_name.setText(QCoreApplication.translate("EditUserWindow", u"Nombre", None))
        self.label_email.setText(QCoreApplication.translate("EditUserWindow", u"Email", None))
        self.label_phone.setText(QCoreApplication.translate("EditUserWindow", u"Telefono", None))
        self.label_address.setText(QCoreApplication.translate("EditUserWindow", u"Direcci\u00f3n", None))
        self.btn_saveuser.setText(QCoreApplication.translate("EditUserWindow", u"Guardar", None))
        self.btn_cancel.setText(QCoreApplication.translate("EditUserWindow", u"Cancelar", None))
    # retranslateUi

