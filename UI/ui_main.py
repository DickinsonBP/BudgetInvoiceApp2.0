# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from Custom_Widgets.Widgets import (QCustomSlideMenu, QCustomStackedWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(974, 600)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	background: transparent;\n"
"	padding: 0;\n"
"	margin: 0;\n"
"	color: #fff;\n"
"}\n"
"#centralwidget, #btn_home , #mainBodyContent,  QLineEdit{\n"
"	background-color: #1b1b27;\n"
"}\n"
"#header, #mainBody {\n"
"	background-color: #27263c;\n"
"}\n"
"#btn_clients, #btn_budgets, #btn_invoices, #btn_search, #btn_adduser {\n"
"	border: 2px solid  #ece424 ;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
" #btn_adduser {\n"
"	border: 2px solid  #ece424 ;\n"
"	background-color: #9c991c ;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QPushButton{\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"#btn_home  {\n"
"	border-left: 3px solid #ece424;\n"
"	font-weight: bold;\n"
"}\n"
"QLineEdit{\n"
"	padding: 5px 10px;\n"
"	border-radius: 10px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QWidget(self.centralwidget)
        self.header.setObjectName(u"header")
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btn_menu = QPushButton(self.frame_2)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"res/Icons/align-justify.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.btn_menu, 0, Qt.AlignLeft)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        self.label.setFont(font)

        self.horizontalLayout_3.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.frame_2, 0, Qt.AlignLeft)

        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_search = QPushButton(self.frame)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMinimumSize(QSize(38, 38))
        self.btn_search.setMaximumSize(QSize(38, 38))
        self.btn_search.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"res/Icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon1)
        self.btn_search.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btn_search)

        self.btn_invoices = QPushButton(self.frame)
        self.btn_invoices.setObjectName(u"btn_invoices")
        self.btn_invoices.setMinimumSize(QSize(38, 38))
        self.btn_invoices.setMaximumSize(QSize(38, 38))
        self.btn_invoices.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"res/Icons/dollar-sign.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_invoices.setIcon(icon2)
        self.btn_invoices.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btn_invoices)

        self.btn_budgets = QPushButton(self.frame)
        self.btn_budgets.setObjectName(u"btn_budgets")
        self.btn_budgets.setMinimumSize(QSize(38, 38))
        self.btn_budgets.setMaximumSize(QSize(38, 38))
        self.btn_budgets.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"res/Icons/file-text.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_budgets.setIcon(icon3)
        self.btn_budgets.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btn_budgets)

        self.btn_clients = QPushButton(self.frame)
        self.btn_clients.setObjectName(u"btn_clients")
        self.btn_clients.setMinimumSize(QSize(38, 38))
        self.btn_clients.setMaximumSize(QSize(38, 38))
        self.btn_clients.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"res/Icons/users.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clients.setIcon(icon4)
        self.btn_clients.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btn_clients)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy)
        self.mainBody.setMinimumSize(QSize(974, 534))
        self.horizontalLayout_4 = QHBoxLayout(self.mainBody)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 9, 0, 0)
        self.leftMenu = QCustomSlideMenu(self.mainBody)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(0, 0))
        self.leftMenu.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 20)
        self.widget = QWidget(self.leftMenu)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(200, 505))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.frame_4)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"res/Icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon5)

        self.verticalLayout_6.addWidget(self.btn_home)

        self.btn_reports = QPushButton(self.frame_4)
        self.btn_reports.setObjectName(u"btn_reports")
        self.btn_reports.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u"res/Icons/printer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reports.setIcon(icon6)

        self.verticalLayout_6.addWidget(self.btn_reports)

        self.btn_account = QPushButton(self.frame_4)
        self.btn_account.setObjectName(u"btn_account")
        self.btn_account.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u"res/Icons/user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_account.setIcon(icon7)

        self.verticalLayout_6.addWidget(self.btn_account)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 10)
        self.btn_settings = QPushButton(self.frame_3)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u"res/Icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon8)

        self.verticalLayout_5.addWidget(self.btn_settings)

        self.btn_help = QPushButton(self.frame_3)
        self.btn_help.setObjectName(u"btn_help")
        self.btn_help.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u"res/Icons/help-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_help.setIcon(icon9)

        self.verticalLayout_5.addWidget(self.btn_help)

        self.btn_about = QPushButton(self.frame_3)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u"res/Icons/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_about.setIcon(icon10)

        self.verticalLayout_5.addWidget(self.btn_about)


        self.verticalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout_4.addWidget(self.leftMenu)

        self.mainBodyContent = QWidget(self.mainBody)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        self.verticalLayout_2 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mainPages = QCustomStackedWidget(self.mainBodyContent)
        self.mainPages.setObjectName(u"mainPages")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.label_6 = QLabel(self.homePage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(280, 220, 201, 91))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_6.setFont(font1)
        self.mainPages.addWidget(self.homePage)
        self.reportsPage = QWidget()
        self.reportsPage.setObjectName(u"reportsPage")
        self.label_3 = QLabel(self.reportsPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(260, 170, 201, 91))
        self.label_3.setFont(font1)
        self.mainPages.addWidget(self.reportsPage)
        self.accountPage = QWidget()
        self.accountPage.setObjectName(u"accountPage")
        self.label_7 = QLabel(self.accountPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(260, 200, 201, 91))
        self.label_7.setFont(font1)
        self.mainPages.addWidget(self.accountPage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.label_4 = QLabel(self.settingsPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(260, 200, 201, 91))
        self.label_4.setFont(font1)
        self.mainPages.addWidget(self.settingsPage)
        self.infoPage = QWidget()
        self.infoPage.setObjectName(u"infoPage")
        self.label_5 = QLabel(self.infoPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(260, 180, 201, 91))
        self.label_5.setFont(font1)
        self.mainPages.addWidget(self.infoPage)
        self.aboutPage = QWidget()
        self.aboutPage.setObjectName(u"aboutPage")
        self.label_8 = QLabel(self.aboutPage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(280, 180, 201, 91))
        self.label_8.setFont(font1)
        self.mainPages.addWidget(self.aboutPage)

        self.verticalLayout_2.addWidget(self.mainPages)


        self.horizontalLayout_4.addWidget(self.mainBodyContent)

        self.rightMenu = QWidget(self.mainBody)
        self.rightMenu.setObjectName(u"rightMenu")
        self.rightMenu.setMinimumSize(QSize(200, 0))
        self.verticalLayout_7 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_2 = QWidget(self.rightMenu)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(70, 70))
        self.label_2.setMaximumSize(QSize(70, 70))
        self.label_2.setPixmap(QPixmap(u"res/Icons/plus-circle.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.frame_5 = QFrame(self.widget_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lineEdit = QLineEdit(self.frame_5)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_9.addWidget(self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame_5)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_9.addWidget(self.lineEdit_2)

        self.lineEdit_3 = QLineEdit(self.frame_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_9.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.frame_5)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_9.addWidget(self.lineEdit_4)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.btn_adduser = QPushButton(self.widget_2)
        self.btn_adduser.setObjectName(u"btn_adduser")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(False)
        self.btn_adduser.setFont(font2)
        self.btn_adduser.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u"res/Icons/thumbs-up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_adduser.setIcon(icon11)
        self.btn_adduser.setIconSize(QSize(24, 24))

        self.verticalLayout_8.addWidget(self.btn_adduser, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.widget_2, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_4.addWidget(self.rightMenu)


        self.verticalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_menu.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Servicios Bedoya", None))
        self.btn_search.setText("")
        self.btn_invoices.setText("")
        self.btn_budgets.setText("")
        self.btn_clients.setText("")
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.btn_reports.setText(QCoreApplication.translate("MainWindow", u"Reportes", None))
        self.btn_account.setText(QCoreApplication.translate("MainWindow", u"Mi cuenta", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Ajustes", None))
        self.btn_help.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.btn_about.setText(QCoreApplication.translate("MainWindow", u"Informacion adicional", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"REPORTS", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ACCOUNT", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"INFO", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ABOUT", None))
        self.label_2.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre de usuario", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NIF", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.btn_adduser.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir Usuario", None))
    # retranslateUi

