# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

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
"#btn_deletebd {\n"
"	border: 2px solid  #FF0000 ;\n"
"	background-color: #DF2929 ;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
" #btn_edituser, #btn_adduser , #btn_deleteuser , #btn_updateUserTable,\n"
"#btn_editbudget, #btn_addbudget , #btn_deletebudget , #btn_updateBudgetTable,\n"
"#btn_editinvoice, #btn_addinvoice , #btn_deleteinvoice , #btn_updateInvoiceTable    {\n"
"	border: 2px solid  #ece424 ;\n"
"	background-color: #D5D042 ;\n"
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
"	border-left: 3px solid #ece4"
                        "24;\n"
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

        self.mainBodyContent = QCustomSlideMenu(self.mainBody)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        self.mainBodyContent.setMinimumSize(QSize(0, 0))
        self.verticalLayout_7 = QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.mainPages = QCustomStackedWidget(self.mainBodyContent)
        self.mainPages.setObjectName(u"mainPages")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_10 = QVBoxLayout(self.homePage)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.homePage)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_11 = QVBoxLayout(self.widget_3)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.widget_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.clients_qty = QLabel(self.frame_6)
        self.clients_qty.setObjectName(u"clients_qty")
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.clients_qty.setFont(font1)

        self.horizontalLayout_6.addWidget(self.clients_qty, 0, Qt.AlignRight)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_6, 0, Qt.AlignLeft)

        self.btn_updateUserTable = QPushButton(self.frame_6)
        self.btn_updateUserTable.setObjectName(u"btn_updateUserTable")
        font2 = QFont()
        font2.setBold(True)
        self.btn_updateUserTable.setFont(font2)
        self.btn_updateUserTable.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u"res/Icons/loader.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_updateUserTable.setIcon(icon7)
        self.btn_updateUserTable.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.btn_updateUserTable)

        self.btn_deleteuser = QPushButton(self.frame_6)
        self.btn_deleteuser.setObjectName(u"btn_deleteuser")
        self.btn_deleteuser.setFont(font2)
        self.btn_deleteuser.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u"res/Icons/frown.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_deleteuser.setIcon(icon8)
        self.btn_deleteuser.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.btn_deleteuser)

        self.btn_edituser = QPushButton(self.frame_6)
        self.btn_edituser.setObjectName(u"btn_edituser")
        self.btn_edituser.setFont(font2)
        self.btn_edituser.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u"res/Icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_edituser.setIcon(icon9)
        self.btn_edituser.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.btn_edituser)

        self.btn_adduser = QPushButton(self.frame_6)
        self.btn_adduser.setObjectName(u"btn_adduser")
        self.btn_adduser.setFont(font2)
        self.btn_adduser.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u"res/Icons/plus-square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_adduser.setIcon(icon10)
        self.btn_adduser.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.btn_adduser)


        self.verticalLayout_11.addWidget(self.frame_6)

        self.table_users = QTableWidget(self.widget_3)
        if (self.table_users.columnCount() < 6):
            self.table_users.setColumnCount(6)
        font3 = QFont()
        font3.setPointSize(30)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        self.table_users.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        self.table_users.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        self.table_users.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        self.table_users.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font3);
        self.table_users.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font3);
        self.table_users.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.table_users.setObjectName(u"table_users")
        font4 = QFont()
        font4.setPointSize(15)
        self.table_users.setFont(font4)

        self.verticalLayout_11.addWidget(self.table_users)


        self.verticalLayout_10.addWidget(self.widget_3)

        self.mainPages.addWidget(self.homePage)
        self.budgetPage = QWidget()
        self.budgetPage.setObjectName(u"budgetPage")
        self.verticalLayout_17 = QVBoxLayout(self.budgetPage)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.budgetPage)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_18 = QVBoxLayout(self.widget_6)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget_6)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.budget_qty = QLabel(self.frame)
        self.budget_qty.setObjectName(u"budget_qty")
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        self.budget_qty.setFont(font5)

        self.horizontalLayout.addWidget(self.budget_qty, 0, Qt.AlignRight)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font5)

        self.horizontalLayout.addWidget(self.label_3)

        self.btn_updateBudgetTable = QPushButton(self.frame)
        self.btn_updateBudgetTable.setObjectName(u"btn_updateBudgetTable")
        font6 = QFont()
        font6.setBold(True)
        font6.setKerning(True)
        self.btn_updateBudgetTable.setFont(font6)
        self.btn_updateBudgetTable.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_updateBudgetTable.setIcon(icon7)
        self.btn_updateBudgetTable.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_updateBudgetTable)

        self.btn_addbudgettemplate = QPushButton(self.frame)
        self.btn_addbudgettemplate.setObjectName(u"btn_addbudgettemplate")
        self.btn_addbudgettemplate.setFont(font2)
        self.btn_addbudgettemplate.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u"res/Icons/plus-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_addbudgettemplate.setIcon(icon11)
        self.btn_addbudgettemplate.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_addbudgettemplate)

        self.btn_deletebudget = QPushButton(self.frame)
        self.btn_deletebudget.setObjectName(u"btn_deletebudget")
        self.btn_deletebudget.setFont(font2)
        self.btn_deletebudget.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_deletebudget.setIcon(icon8)
        self.btn_deletebudget.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_deletebudget)

        self.btn_editbudget = QPushButton(self.frame)
        self.btn_editbudget.setObjectName(u"btn_editbudget")
        self.btn_editbudget.setFont(font2)
        self.btn_editbudget.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_editbudget.setIcon(icon9)
        self.btn_editbudget.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_editbudget)

        self.btn_addbudget = QPushButton(self.frame)
        self.btn_addbudget.setObjectName(u"btn_addbudget")
        self.btn_addbudget.setFont(font2)
        self.btn_addbudget.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_addbudget.setIcon(icon10)
        self.btn_addbudget.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_addbudget)


        self.verticalLayout_18.addWidget(self.frame)


        self.verticalLayout_17.addWidget(self.widget_6)

        self.table_budgets = QTableWidget(self.budgetPage)
        if (self.table_budgets.columnCount() < 7):
            self.table_budgets.setColumnCount(7)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_budgets.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_budgets.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_budgets.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_budgets.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_budgets.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_budgets.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_budgets.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        self.table_budgets.setObjectName(u"table_budgets")
        font7 = QFont()
        font7.setPointSize(15)
        font7.setBold(False)
        self.table_budgets.setFont(font7)

        self.verticalLayout_17.addWidget(self.table_budgets)

        self.mainPages.addWidget(self.budgetPage)
        self.invoicePage = QWidget()
        self.invoicePage.setObjectName(u"invoicePage")
        self.verticalLayout_8 = QVBoxLayout(self.invoicePage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_2 = QWidget(self.invoicePage)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_9 = QVBoxLayout(self.widget_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_5 = QFrame(self.widget_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.invoices_qty = QLabel(self.frame_5)
        self.invoices_qty.setObjectName(u"invoices_qty")

        self.horizontalLayout_7.addWidget(self.invoices_qty, 0, Qt.AlignRight)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_2, 0, Qt.AlignLeft)

        self.btn_updateInvoiceTable = QPushButton(self.frame_5)
        self.btn_updateInvoiceTable.setObjectName(u"btn_updateInvoiceTable")
        self.btn_updateInvoiceTable.setFont(font2)
        self.btn_updateInvoiceTable.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_updateInvoiceTable.setIcon(icon7)
        self.btn_updateInvoiceTable.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.btn_updateInvoiceTable)

        self.btn_deleteinvoice = QPushButton(self.frame_5)
        self.btn_deleteinvoice.setObjectName(u"btn_deleteinvoice")
        self.btn_deleteinvoice.setIcon(icon8)
        self.btn_deleteinvoice.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.btn_deleteinvoice)

        self.btn_editinvoice = QPushButton(self.frame_5)
        self.btn_editinvoice.setObjectName(u"btn_editinvoice")
        self.btn_editinvoice.setIcon(icon9)
        self.btn_editinvoice.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.btn_editinvoice)

        self.btn_addinvoice = QPushButton(self.frame_5)
        self.btn_addinvoice.setObjectName(u"btn_addinvoice")
        icon12 = QIcon()
        icon12.addFile(u"../res/Icons/plus-square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_addinvoice.setIcon(icon12)
        self.btn_addinvoice.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.btn_addinvoice)


        self.verticalLayout_9.addWidget(self.frame_5)

        self.table_invoices = QTableWidget(self.widget_2)
        if (self.table_invoices.columnCount() < 6):
            self.table_invoices.setColumnCount(6)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_invoices.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_invoices.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_invoices.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_invoices.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_invoices.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_invoices.setHorizontalHeaderItem(5, __qtablewidgetitem18)
        self.table_invoices.setObjectName(u"table_invoices")
        self.table_invoices.setFont(font4)

        self.verticalLayout_9.addWidget(self.table_invoices)


        self.verticalLayout_8.addWidget(self.widget_2)

        self.mainPages.addWidget(self.invoicePage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.verticalLayout_14 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.settingsPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_14.addWidget(self.label_4)

        self.btn_deletebd = QPushButton(self.settingsPage)
        self.btn_deletebd.setObjectName(u"btn_deletebd")
        font8 = QFont()
        font8.setPointSize(20)
        font8.setBold(True)
        self.btn_deletebd.setFont(font8)
        self.btn_deletebd.setIconSize(QSize(30, 30))

        self.verticalLayout_14.addWidget(self.btn_deletebd, 0, Qt.AlignHCenter)

        self.mainPages.addWidget(self.settingsPage)

        self.verticalLayout_7.addWidget(self.mainPages)


        self.horizontalLayout_4.addWidget(self.mainBodyContent)


        self.verticalLayout.addWidget(self.mainBody)

        self.footer = QWidget(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.horizontalLayout_5 = QHBoxLayout(self.footer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_9 = QLabel(self.footer)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font5)

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
        self.clients_qty.setText(QCoreApplication.translate("MainWindow", u"#", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CLIENTES", None))
        self.btn_updateUserTable.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btn_deleteuser.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.btn_edituser.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_adduser.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir", None))
        ___qtablewidgetitem = self.table_users.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Identificador", None));
        ___qtablewidgetitem1 = self.table_users.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NIF", None));
        ___qtablewidgetitem2 = self.table_users.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem3 = self.table_users.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem4 = self.table_users.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None));
        ___qtablewidgetitem5 = self.table_users.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Telefono", None));
        self.budget_qty.setText(QCoreApplication.translate("MainWindow", u"#", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PRESUPUESTOS", None))
        self.btn_updateBudgetTable.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btn_addbudgettemplate.setText(QCoreApplication.translate("MainWindow", u"Nueva Plantilla", None))
        self.btn_deletebudget.setText(QCoreApplication.translate("MainWindow", u"Eliminar Presupuesto", None))
        self.btn_editbudget.setText(QCoreApplication.translate("MainWindow", u"Editar Presupuesto", None))
        self.btn_addbudget.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        ___qtablewidgetitem6 = self.table_budgets.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Identificador", None));
        ___qtablewidgetitem7 = self.table_budgets.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Numero de presupuesto", None));
        ___qtablewidgetitem8 = self.table_budgets.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Titulo", None));
        ___qtablewidgetitem9 = self.table_budgets.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem10 = self.table_budgets.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem11 = self.table_budgets.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None));
        ___qtablewidgetitem12 = self.table_budgets.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Locaclizaci\u00f3n del archivo", None));
        self.invoices_qty.setText(QCoreApplication.translate("MainWindow", u"#", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Facturas", None))
        self.btn_updateInvoiceTable.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btn_deleteinvoice.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.btn_editinvoice.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_addinvoice.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir", None))
        ___qtablewidgetitem13 = self.table_invoices.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Identificador", None));
        ___qtablewidgetitem14 = self.table_invoices.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Numero de factura", None));
        ___qtablewidgetitem15 = self.table_invoices.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Titulo", None));
        ___qtablewidgetitem16 = self.table_invoices.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem17 = self.table_invoices.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem18 = self.table_invoices.horizontalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"AJUSTES", None))
        self.btn_deletebd.setText(QCoreApplication.translate("MainWindow", u"BORRAR BASE DE DATOS", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Servicios Bedoya. Copyright 2023", None))
    # retranslateUi

