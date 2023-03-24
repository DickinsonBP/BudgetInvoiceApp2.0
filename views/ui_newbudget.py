# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_newbudget.ui'
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

from Custom_Widgets.Widgets import QCustomStackedWidget

class Ui_NewBudgetWindow(object):
    def setupUi(self, NewBudgetWindow):
        if not NewBudgetWindow.objectName():
            NewBudgetWindow.setObjectName(u"NewBudgetWindow")
        NewBudgetWindow.resize(700, 650)
        NewBudgetWindow.setStyleSheet(u"*{\n"
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
"QPushButton  {\n"
"	border: 2px solid  #ece424 ;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton  {\n"
"	border: 2px solid  #ece424 ;\n"
"	background-color: #9c991c ;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
" QPushButton:pressed   {\n"
"	background-color: #9C995F ;\n"
"}")
        self.verticalLayout = QVBoxLayout(NewBudgetWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.centralwidget = QWidget(NewBudgetWindow)
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

        self.budgetPages = QCustomStackedWidget(self.widget)
        self.budgetPages.setObjectName(u"budgetPages")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_4 = QVBoxLayout(self.home_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.home_page)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setBold(True)
        self.label_2.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_2)

        self.line_budgetNumber = QLineEdit(self.home_page)
        self.line_budgetNumber.setObjectName(u"line_budgetNumber")

        self.verticalLayout_4.addWidget(self.line_budgetNumber, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.home_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_3)

        self.line_title = QLineEdit(self.home_page)
        self.line_title.setObjectName(u"line_title")

        self.verticalLayout_4.addWidget(self.line_title)

        self.label_4 = QLabel(self.home_page)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.budget_date = QDateEdit(self.home_page)
        self.budget_date.setObjectName(u"budget_date")

        self.verticalLayout_4.addWidget(self.budget_date, 0, Qt.AlignHCenter)

        self.label_5 = QLabel(self.home_page)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5)

        self.widget_2 = QWidget(self.home_page)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.user_combobox = QComboBox(self.widget_2)
        self.user_combobox.setObjectName(u"user_combobox")

        self.horizontalLayout_2.addWidget(self.user_combobox)

        self.btn_newuser = QPushButton(self.widget_2)
        self.btn_newuser.setObjectName(u"btn_newuser")
        self.btn_newuser.setFont(font1)
        self.btn_newuser.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"res/Icons/check-square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_newuser.setIcon(icon)
        self.btn_newuser.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_newuser, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.widget_2)

        self.label_6 = QLabel(self.home_page)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_4.addWidget(self.label_6)

        self.widget_3 = QWidget(self.home_page)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.line_address = QLineEdit(self.widget_3)
        self.line_address.setObjectName(u"line_address")

        self.horizontalLayout_3.addWidget(self.line_address)

        self.btn_clientaddress = QPushButton(self.widget_3)
        self.btn_clientaddress.setObjectName(u"btn_clientaddress")
        self.btn_clientaddress.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_clientaddress.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.btn_clientaddress)


        self.verticalLayout_4.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.home_page)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_continue = QPushButton(self.widget_4)
        self.btn_continue.setObjectName(u"btn_continue")
        self.btn_continue.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"res/Icons/smile.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_continue.setIcon(icon1)
        self.btn_continue.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.btn_continue, 0, Qt.AlignHCenter)

        self.btn_cancel = QPushButton(self.widget_4)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"res/Icons/frown.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cancel.setIcon(icon2)
        self.btn_cancel.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.btn_cancel, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.widget_4)

        self.budgetPages.addWidget(self.home_page)
        self.edit_data = QWidget()
        self.edit_data.setObjectName(u"edit_data")
        self.verticalLayout_5 = QVBoxLayout(self.edit_data)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_2 = QFrame(self.edit_data)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_7, 0, Qt.AlignHCenter)

        self.budget_number = QLabel(self.frame_2)
        self.budget_number.setObjectName(u"budget_number")
        self.budget_number.setFont(font)

        self.horizontalLayout_5.addWidget(self.budget_number, 0, Qt.AlignLeft)


        self.verticalLayout_5.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.description_widget = QWidget(self.edit_data)
        self.description_widget.setObjectName(u"description_widget")
        self.verticalLayout_6 = QVBoxLayout(self.description_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_newrow = QPushButton(self.description_widget)
        self.btn_newrow.setObjectName(u"btn_newrow")

        self.verticalLayout_6.addWidget(self.btn_newrow, 0, Qt.AlignLeft)

        self.data_widget_1 = QWidget(self.description_widget)
        self.data_widget_1.setObjectName(u"data_widget_1")
        self.horizontalLayout_7 = QHBoxLayout(self.data_widget_1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.combobox_type_1 = QComboBox(self.data_widget_1)
        self.combobox_type_1.setObjectName(u"combobox_type_1")

        self.horizontalLayout_7.addWidget(self.combobox_type_1)

        self.line_desc_1 = QLineEdit(self.data_widget_1)
        self.line_desc_1.setObjectName(u"line_desc_1")

        self.horizontalLayout_7.addWidget(self.line_desc_1)

        self.line_price_1 = QLineEdit(self.data_widget_1)
        self.line_price_1.setObjectName(u"line_price_1")

        self.horizontalLayout_7.addWidget(self.line_price_1, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.data_widget_1)


        self.verticalLayout_5.addWidget(self.description_widget)

        self.widget_7 = QWidget(self.edit_data)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(self.widget_7)
        self.label_12.setObjectName(u"label_12")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.label_12.setFont(font2)

        self.horizontalLayout_8.addWidget(self.label_12)

        self.line_total = QLineEdit(self.widget_7)
        self.line_total.setObjectName(u"line_total")

        self.horizontalLayout_8.addWidget(self.line_total, 0, Qt.AlignHCenter)

        self.label_11 = QLabel(self.widget_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_11, 0, Qt.AlignRight)

        self.comboBox_vat = QComboBox(self.widget_7)
        self.comboBox_vat.setObjectName(u"comboBox_vat")

        self.horizontalLayout_8.addWidget(self.comboBox_vat)

        self.label_total = QLabel(self.widget_7)
        self.label_total.setObjectName(u"label_total")
        self.label_total.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_total)


        self.verticalLayout_5.addWidget(self.widget_7, 0, Qt.AlignBottom)

        self.widget_8 = QWidget(self.edit_data)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_save = QPushButton(self.widget_8)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.btn_save, 0, Qt.AlignHCenter)

        self.btn_back = QPushButton(self.widget_8)
        self.btn_back.setObjectName(u"btn_back")
        self.btn_back.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_back.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.btn_back, 0, Qt.AlignHCenter)

        self.btn_cancel2 = QPushButton(self.widget_8)
        self.btn_cancel2.setObjectName(u"btn_cancel2")

        self.horizontalLayout_6.addWidget(self.btn_cancel2, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.widget_8, 0, Qt.AlignBottom)

        self.budgetPages.addWidget(self.edit_data)

        self.verticalLayout_3.addWidget(self.budgetPages)


        self.verticalLayout_2.addWidget(self.widget)


        self.verticalLayout.addWidget(self.centralwidget)


        self.retranslateUi(NewBudgetWindow)

        QMetaObject.connectSlotsByName(NewBudgetWindow)
    # setupUi

    def retranslateUi(self, NewBudgetWindow):
        NewBudgetWindow.setWindowTitle(QCoreApplication.translate("NewBudgetWindow", u"Nuevo Presupuesto", None))
        self.label.setText(QCoreApplication.translate("NewBudgetWindow", u"Nuevo Presupuesto", None))
        self.label_2.setText(QCoreApplication.translate("NewBudgetWindow", u"Numero de presupuesto", None))
        self.label_3.setText(QCoreApplication.translate("NewBudgetWindow", u"Titulo", None))
        self.label_4.setText(QCoreApplication.translate("NewBudgetWindow", u"Fecha", None))
        self.label_5.setText(QCoreApplication.translate("NewBudgetWindow", u"Cliente", None))
        self.btn_newuser.setText(QCoreApplication.translate("NewBudgetWindow", u"Nuevo cliente", None))
        self.label_6.setText(QCoreApplication.translate("NewBudgetWindow", u"Direcci\u00f3n", None))
        self.btn_clientaddress.setText(QCoreApplication.translate("NewBudgetWindow", u"Usar direcci\u00f3n del cliente", None))
        self.btn_continue.setText(QCoreApplication.translate("NewBudgetWindow", u"Continuar", None))
        self.btn_cancel.setText(QCoreApplication.translate("NewBudgetWindow", u"Cancelar", None))
        self.label_7.setText(QCoreApplication.translate("NewBudgetWindow", u"Presupuesto N\u00b0", None))
        self.budget_number.setText(QCoreApplication.translate("NewBudgetWindow", u"#", None))
        self.btn_newrow.setText(QCoreApplication.translate("NewBudgetWindow", u"A\u00f1adir fila", None))
        self.combobox_type_1.setPlaceholderText(QCoreApplication.translate("NewBudgetWindow", u"Tipo", None))
        self.line_desc_1.setPlaceholderText(QCoreApplication.translate("NewBudgetWindow", u"Descripci\u00f3n", None))
        self.line_price_1.setPlaceholderText(QCoreApplication.translate("NewBudgetWindow", u"Precio", None))
        self.label_12.setText(QCoreApplication.translate("NewBudgetWindow", u"Precio total", None))
        self.label_11.setText(QCoreApplication.translate("NewBudgetWindow", u"IIVA", None))
        self.label_total.setText(QCoreApplication.translate("NewBudgetWindow", u"#", None))
        self.btn_save.setText(QCoreApplication.translate("NewBudgetWindow", u"Guardar", None))
        self.btn_back.setText(QCoreApplication.translate("NewBudgetWindow", u"Volver", None))
        self.btn_cancel2.setText(QCoreApplication.translate("NewBudgetWindow", u"Cancelar", None))
    # retranslateUi

