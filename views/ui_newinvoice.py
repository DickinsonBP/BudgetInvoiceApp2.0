# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_newinvoice.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_NewInvoiceWindow(object):
    def setupUi(self, NewInvoiceWindow):
        if not NewInvoiceWindow.objectName():
            NewInvoiceWindow.setObjectName(u"NewInvoiceWindow")
        NewInvoiceWindow.resize(700, 650)
        NewInvoiceWindow.setStyleSheet(u"*{\n"
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
"#btn_saveinvoice, #btn_cance , #btn_newuser , #btn_clientaddress  {\n"
"	border: 2px solid  #ece424 ;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
" #btn_saveinvoice, #btn_cancel , #btn_newuser , #btn_clientaddress  {\n"
"	border: 2px solid  #ece424 ;\n"
"	background-color: #9c991c ;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
" #btn_saveinvoice:pressed, #btn_cancel:pressed   {\n"
"	background-color: #9C995F ;\n"
"}")
        self.verticalLayout = QVBoxLayout(NewInvoiceWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.centralwidget = QWidget(NewInvoiceWindow)
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
        font.setPointSize(25)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.frame)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_invoicenumber = QLabel(self.widget_2)
        self.label_invoicenumber.setObjectName(u"label_invoicenumber")
        font1 = QFont()
        font1.setBold(True)
        self.label_invoicenumber.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_invoicenumber)

        self.line_invoicenumber = QLineEdit(self.widget_2)
        self.line_invoicenumber.setObjectName(u"line_invoicenumber")

        self.verticalLayout_4.addWidget(self.line_invoicenumber, 0, Qt.AlignHCenter)

        self.label_invoicetitle = QLabel(self.widget_2)
        self.label_invoicetitle.setObjectName(u"label_invoicetitle")
        self.label_invoicetitle.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_invoicetitle)

        self.line_title = QLineEdit(self.widget_2)
        self.line_title.setObjectName(u"line_title")

        self.verticalLayout_4.addWidget(self.line_title)

        self.label_date = QLabel(self.widget_2)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_date)

        self.budget_date = QDateEdit(self.widget_2)
        self.budget_date.setObjectName(u"budget_date")

        self.verticalLayout_4.addWidget(self.budget_date, 0, Qt.AlignHCenter)

        self.label_client = QLabel(self.widget_2)
        self.label_client.setObjectName(u"label_client")
        self.label_client.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_client)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.user_comobox = QComboBox(self.widget_4)
        self.user_comobox.setObjectName(u"user_comobox")

        self.horizontalLayout_3.addWidget(self.user_comobox)

        self.btn_newuser = QPushButton(self.widget_4)
        self.btn_newuser.setObjectName(u"btn_newuser")
        self.btn_newuser.setFont(font1)
        self.btn_newuser.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"res/Icons/check-square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_newuser.setIcon(icon)
        self.btn_newuser.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.btn_newuser, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.widget_4)

        self.label_address = QLabel(self.widget_2)
        self.label_address.setObjectName(u"label_address")
        self.label_address.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_address)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.line_address = QLineEdit(self.widget_5)
        self.line_address.setObjectName(u"line_address")

        self.horizontalLayout_4.addWidget(self.line_address)

        self.btn_clientaddress = QPushButton(self.widget_5)
        self.btn_clientaddress.setObjectName(u"btn_clientaddress")

        self.horizontalLayout_4.addWidget(self.btn_clientaddress)


        self.verticalLayout_4.addWidget(self.widget_5)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_saveinvoice = QPushButton(self.widget_3)
        self.btn_saveinvoice.setObjectName(u"btn_saveinvoice")
        self.btn_saveinvoice.setFont(font1)
        self.btn_saveinvoice.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"res/Icons/check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_saveinvoice.setIcon(icon1)
        self.btn_saveinvoice.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_saveinvoice, 0, Qt.AlignHCenter)

        self.btn_cancel = QPushButton(self.widget_3)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setFont(font1)
        self.btn_cancel.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"res/Icons/thumbs-down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cancel.setIcon(icon2)
        self.btn_cancel.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_cancel, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.widget_3)


        self.verticalLayout_3.addWidget(self.widget_2)


        self.verticalLayout_2.addWidget(self.widget)


        self.verticalLayout.addWidget(self.centralwidget)


        self.retranslateUi(NewInvoiceWindow)

        QMetaObject.connectSlotsByName(NewInvoiceWindow)
    # setupUi

    def retranslateUi(self, NewInvoiceWindow):
        NewInvoiceWindow.setWindowTitle(QCoreApplication.translate("NewInvoiceWindow", u"Nueva Factura", None))
        self.label.setText(QCoreApplication.translate("NewInvoiceWindow", u"Nueva Factura", None))
        self.label_invoicenumber.setText(QCoreApplication.translate("NewInvoiceWindow", u"Numero de factura", None))
        self.label_invoicetitle.setText(QCoreApplication.translate("NewInvoiceWindow", u"Titulo de la factura", None))
        self.label_date.setText(QCoreApplication.translate("NewInvoiceWindow", u"Fecha", None))
        self.label_client.setText(QCoreApplication.translate("NewInvoiceWindow", u"Cliente", None))
        self.btn_newuser.setText(QCoreApplication.translate("NewInvoiceWindow", u"Nuevo cliente", None))
        self.label_address.setText(QCoreApplication.translate("NewInvoiceWindow", u"Direcci\u00f3n", None))
        self.btn_clientaddress.setText(QCoreApplication.translate("NewInvoiceWindow", u"Usar direcci\u00f3n del cliente", None))
        self.btn_saveinvoice.setText(QCoreApplication.translate("NewInvoiceWindow", u"Guardar", None))
        self.btn_cancel.setText(QCoreApplication.translate("NewInvoiceWindow", u"Cancelar", None))
    # retranslateUi

