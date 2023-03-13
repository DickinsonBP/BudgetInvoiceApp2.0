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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

from Custom_Widgets.Widgets import (QCustomSlideMenu, QCustomStackedWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(974, 650)
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
"#header, #mainBody, #footer {\n"
"	background-color: #27263c;\n"
"}\n"
"#btn_clients, #btn_adduser, #btn_deletesuser, #btn_edituser  {\n"
"	border: 2px solid  #ece424 ;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
" #btn_adduser,#btn_deleteuser, #btn_edituser   {\n"
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
        self.leftMenu.setMinimumSize(QSize(200, 0))
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
        self.btn_home.setStyleSheet(u"background-color: #1b1b27;")
        icon1 = QIcon()
        icon1.addFile(u"res/Icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon1)

        self.verticalLayout_6.addWidget(self.btn_home)

        self.btn_budgets = QPushButton(self.frame_4)
        self.btn_budgets.setObjectName(u"btn_budgets")
        self.btn_budgets.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"res/Icons/file-text.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_budgets.setIcon(icon2)

        self.verticalLayout_6.addWidget(self.btn_budgets)

        self.btn_invoices = QPushButton(self.frame_4)
        self.btn_invoices.setObjectName(u"btn_invoices")
        self.btn_invoices.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"res/Icons/dollar-sign.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_invoices.setIcon(icon3)

        self.verticalLayout_6.addWidget(self.btn_invoices)


        self.verticalLayout_4.addWidget(self.frame_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_settings = QPushButton(self.frame_3)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"res/Icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon4)

        self.verticalLayout_5.addWidget(self.btn_settings)

        self.btn_help = QPushButton(self.frame_3)
        self.btn_help.setObjectName(u"btn_help")
        self.btn_help.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u"res/Icons/help-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_help.setIcon(icon5)

        self.verticalLayout_5.addWidget(self.btn_help)

        self.btn_about = QPushButton(self.frame_3)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u"res/Icons/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_about.setIcon(icon6)

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
        self.verticalLayout_10 = QVBoxLayout(self.homePage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_3 = QWidget(self.homePage)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_11 = QVBoxLayout(self.widget_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_6 = QFrame(self.widget_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_6.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_6, 0, Qt.AlignLeft)

        self.btn_showUserForm = QPushButton(self.frame_6)
        self.btn_showUserForm.setObjectName(u"btn_showUserForm")
        font2 = QFont()
        font2.setBold(True)
        self.btn_showUserForm.setFont(font2)
        self.btn_showUserForm.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u"res/Icons/plus-square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_showUserForm.setIcon(icon7)
        self.btn_showUserForm.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.btn_showUserForm, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_6)

        self.tableWidget = QTableWidget(self.widget_3)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        font3 = QFont()
        font3.setPointSize(30)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        font4 = QFont()
        font4.setPointSize(15)
        self.tableWidget.setFont(font4)

        self.verticalLayout_11.addWidget(self.tableWidget)


        self.verticalLayout_10.addWidget(self.widget_3)

        self.mainPages.addWidget(self.homePage)
        self.budgetPage = QWidget()
        self.budgetPage.setObjectName(u"budgetPage")
        self.verticalLayout_17 = QVBoxLayout(self.budgetPage)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.widget_6 = QWidget(self.budgetPage)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_18 = QVBoxLayout(self.widget_6)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame = QFrame(self.widget_6)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout.addWidget(self.label_3)

        self.btn_addbudgettemplate = QPushButton(self.frame)
        self.btn_addbudgettemplate.setObjectName(u"btn_addbudgettemplate")
        self.btn_addbudgettemplate.setFont(font2)
        self.btn_addbudgettemplate.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u"res/Icons/plus-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_addbudgettemplate.setIcon(icon8)
        self.btn_addbudgettemplate.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_addbudgettemplate, 0, Qt.AlignRight)

        self.btn_addbudget = QPushButton(self.frame)
        self.btn_addbudget.setObjectName(u"btn_addbudget")
        self.btn_addbudget.setFont(font2)
        self.btn_addbudget.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_addbudget.setIcon(icon7)
        self.btn_addbudget.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_addbudget, 0, Qt.AlignRight)


        self.verticalLayout_18.addWidget(self.frame)


        self.verticalLayout_17.addWidget(self.widget_6)

        self.tableWidget_2 = QTableWidget(self.budgetPage)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout_17.addWidget(self.tableWidget_2)

        self.mainPages.addWidget(self.budgetPage)
        self.invoicePage = QWidget()
        self.invoicePage.setObjectName(u"invoicePage")
        self.label_7 = QLabel(self.invoicePage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(260, 200, 201, 91))
        self.label_7.setFont(font1)
        self.mainPages.addWidget(self.invoicePage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.verticalLayout_14 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_4 = QLabel(self.settingsPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_14.addWidget(self.label_4)

        self.label_10 = QLabel(self.settingsPage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font4)

        self.verticalLayout_14.addWidget(self.label_10)

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

        self.rightMenu = QCustomSlideMenu(self.mainBody)
        self.rightMenu.setObjectName(u"rightMenu")
        self.rightMenu.setMinimumSize(QSize(200, 0))
        self.verticalLayout_7 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_2 = QWidget(self.rightMenu)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(162, 286))
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
        self.userName = QLineEdit(self.frame_5)
        self.userName.setObjectName(u"userName")

        self.verticalLayout_9.addWidget(self.userName)

        self.nif = QLineEdit(self.frame_5)
        self.nif.setObjectName(u"nif")

        self.verticalLayout_9.addWidget(self.nif)

        self.email = QLineEdit(self.frame_5)
        self.email.setObjectName(u"email")

        self.verticalLayout_9.addWidget(self.email)

        self.address = QLineEdit(self.frame_5)
        self.address.setObjectName(u"address")

        self.verticalLayout_9.addWidget(self.address)

        self.phone = QLineEdit(self.frame_5)
        self.phone.setObjectName(u"phone")

        self.verticalLayout_9.addWidget(self.phone)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.btn_adduser = QPushButton(self.widget_2)
        self.btn_adduser.setObjectName(u"btn_adduser")
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setItalic(False)
        self.btn_adduser.setFont(font5)
        self.btn_adduser.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u"res/Icons/thumbs-up.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_adduser.setIcon(icon9)
        self.btn_adduser.setIconSize(QSize(24, 24))

        self.verticalLayout_8.addWidget(self.btn_adduser, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.widget_2, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.widget_4 = QWidget(self.rightMenu)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_12 = QVBoxLayout(self.widget_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_7 = QFrame(self.widget_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_7)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.nif_2 = QLineEdit(self.frame_7)
        self.nif_2.setObjectName(u"nif_2")

        self.verticalLayout_13.addWidget(self.nif_2)


        self.verticalLayout_12.addWidget(self.frame_7)

        self.btn_deleteuser = QPushButton(self.widget_4)
        self.btn_deleteuser.setObjectName(u"btn_deleteuser")
        self.btn_deleteuser.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u"res/Icons/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_deleteuser.setIcon(icon10)
        self.btn_deleteuser.setIconSize(QSize(24, 24))

        self.verticalLayout_12.addWidget(self.btn_deleteuser)


        self.verticalLayout_7.addWidget(self.widget_4, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.widget_5 = QWidget(self.rightMenu)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_15 = QVBoxLayout(self.widget_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_8 = QFrame(self.widget_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_8)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.nif_3 = QLineEdit(self.frame_8)
        self.nif_3.setObjectName(u"nif_3")

        self.verticalLayout_16.addWidget(self.nif_3)


        self.verticalLayout_15.addWidget(self.frame_8)

        self.btn_edituser = QPushButton(self.widget_5)
        self.btn_edituser.setObjectName(u"btn_edituser")
        icon11 = QIcon()
        icon11.addFile(u"res/Icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_edituser.setIcon(icon11)
        self.btn_edituser.setIconSize(QSize(24, 24))

        self.verticalLayout_15.addWidget(self.btn_edituser)


        self.verticalLayout_7.addWidget(self.widget_5, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_4.addWidget(self.rightMenu)


        self.verticalLayout.addWidget(self.mainBody)

        self.footer = QWidget(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.horizontalLayout_5 = QHBoxLayout(self.footer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_9 = QLabel(self.footer)
        self.label_9.setObjectName(u"label_9")
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        self.label_9.setFont(font6)

        self.horizontalLayout_5.addWidget(self.label_9, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_menu.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Servicios Bedoya", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.btn_budgets.setText(QCoreApplication.translate("MainWindow", u"Presupuestos", None))
        self.btn_invoices.setText(QCoreApplication.translate("MainWindow", u"Facturas", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Ajustes", None))
        self.btn_help.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.btn_about.setText(QCoreApplication.translate("MainWindow", u"Informacion adicional", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"INICIO", None))
        self.btn_showUserForm.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir usuario", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Identificador", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NIF", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Telefono", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PRESUPUESTOS", None))
        self.btn_addbudgettemplate.setText(QCoreApplication.translate("MainWindow", u"Nueva Plantilla", None))
        self.btn_addbudget.setText(QCoreApplication.translate("MainWindow", u"Nuevo Presupuesto", None))
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Identificador", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Facturas", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"AJUSTES", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"De momento no se puede hacer nada...", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"INFO", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ABOUT", None))
        self.label_2.setText("")
        self.userName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nombre de usuario", None))
        self.nif.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NIF", None))
        self.email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.address.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None))
        self.phone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.btn_adduser.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir Usuario", None))
        self.nif_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NIF", None))
        self.btn_deleteuser.setText(QCoreApplication.translate("MainWindow", u"Eliminar Usuario", None))
        self.nif_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NIF", None))
        self.btn_edituser.setText(QCoreApplication.translate("MainWindow", u"Editar usuario", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Servicios Bedoya. Copyright 2023", None))
    # retranslateUi

