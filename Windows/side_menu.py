from PySide6.QtCore import Qt, QAbstractListModel, QSize, QRect
from PySide6.QtGui import QPainter, QPixmap, QFont, QColor
from PySide6.QtWidgets import (QMdiSubWindow, QWidget, QGraphicsDropShadowEffect, QStyleOption, QStyle, QVBoxLayout,QHBoxLayout, QListView, QFrame,
                                QStyledItemDelegate, QLabel, QPushButton)


class Delegate(QStyledItemDelegate):
    def __init__(self, height=None):
        super(Delegate, self).__init__()
        if height is None:
            self._height = 45
        else:
            self._height = height

    def paint(self, painter, option, index):
        super(Delegate, self).paint(painter, option, index)

        # HOVER
        #if option.state & QStyle.State_MouseOver:
        #    painter.fillRect(option.rect, QColor("#F1F1F1"))
        #else:
        #    painter.fillRect(option.rect, Qt.transparent)

        # SELECTED
        #if option.state & QStyle.State_Selected:
        #    painter.fillRect(option.rect, QColor("#F1F1F1"))

        # DRAW ICON
        icon = QPixmap()
        icon.load(index.data()[1])
        icon = icon.scaled(24, 24, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

        left = 24 # margin left
        icon_pos = QRect(left, ((self._height - icon.height()) / 2) + option.rect.y(), icon.width(), icon.height())
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.drawPixmap(icon_pos, icon)

        # DRAW TEXT
        font = QFont("Roboto Black", 12)
        text_pos = QRect((left * 2) + icon.width(), option.rect.y(), option.rect.width(), option.rect.height())
        painter.setFont(font)
        painter.setPen(Qt.black)
        painter.drawText(text_pos, Qt.AlignVCenter, index.data()[0])

    def sizeHint(self, option, index):
        return QSize(0, self._height)


class Model(QAbstractListModel):
    def __init__(self, data=None):
        super(Model, self).__init__()
        if data is None:
            data = [
                ("Clientes", "res/img/icons/group.png"),
                ("Presupuestos", "res/img/icons/settings.png"),
                ("Facturas", "res/img/icons/moon.png")
            ]
        self._data = data

    def rowCount(self, index):
        return len(self._data)

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid() and role == Qt.DisplayRole:
            return self._data[index.row()]


class ListView(QListView):
    def __init__(self):
        super(ListView, self).__init__()
        #self.setMouseTracking(True)
        
    def mouseMoveEvent(self, event):
        # CHANGE CURSOR HOVERING
        if self.indexAt(event.pos()).row() >= 0:
            self.setCursor(Qt.PointingHandCursor)
        else:
            self.setCursor(Qt.ArrowCursor)


class LinkLabel(QLabel):
    def __init__(self, parent=None, leave=None, enter=None):
        super(LinkLabel, self).__init__(parent)
        if leave is not None and enter is not None:
            self.setStyleSheet(leave)
            self.leave = leave
            self.enter = enter
        else:
            self.leave = "color: rgba(0, 0, 0, 100%);"
            self.enter = "color: rgba(0, 0, 0, 100%);"
            self.setStyleSheet(self.leave)
        self.setCursor(Qt.PointingHandCursor)

    def enterEvent(self, event):
        self.setStyleSheet("{}; text-decoration: underline;".format(self.enter))

    def leaveEvent(self, event):
        self.setStyleSheet("{}; text-decoration: none;".format(self.leave))


class Profile(QWidget):
    def __init__(self, height=None):
        super(Profile, self).__init__()
        if height is None:
            self.setFixedHeight(150)
        else:
            self.setFixedHeight(height)

    def paintEvent(self, event):
        super(Profile, self).paintEvent(event)

        # DRAW BACKGROUND IMAGE
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        image = QPixmap()
        image.load("res/img/logo.png")
        image = image.scaled(self.width(), self.height(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        p.drawPixmap(self.rect(), image)


class SideMenuWidget(QWidget):
    def __init__(self):
        super(SideMenuWidget, self).__init__()
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(12)
        self.setLayout(self.layout)

        # PROFILE
        self.layout.addWidget(Profile())

        # BUTTONS
        self.listview = ListView()
        self.listview.setFrameStyle(QFrame.NoFrame)
        self.listview.setFocusPolicy(Qt.NoFocus)
        self.listview.setModel(Model())
        self.listview.setItemDelegate(Delegate())
        self.listview.clicked.connect(self.button_budget)
        self.layout.addWidget(self.listview)

        # LABELS
        self.labels = QWidget()
        self.labels.setFixedHeight(60)
        self.layout.addWidget(self.labels)

        _margins = 16 # left margin

        self.app_name = LinkLabel(self.labels, "color: rgba(0, 0, 0, 80%)", "color: rgba(0, 0, 0, 60%)")
        self.app_name.setText("Servicios Bedoya")
        self.app_name.setFont(QFont("Roboto Light", 12))
        self.app_name.move(self.labels.x() + _margins, self.labels.y())

        self.app_ver = LinkLabel(self.labels, "color: rgba(0, 0, 0, 60%)", "color: rgba(0, 0, 0, 60%)")
        self.app_ver.setText("")
        self.app_ver.setFont(QFont("Roboto Light", 11))
        self.app_ver.move(self.labels.x() + _margins, self.labels.y() + _margins * 2)

        self.lbl = QLabel(self.labels)
        self.lbl.setText("-")
        self.lbl.setStyleSheet("color: rgba(0, 0, 0, 60%)")
        self.lbl.setFont(QFont("Roboto Light", 11))
        self.lbl.move(self.labels.x() + _margins * 7, self.labels.y() + _margins * 2)

        self.app_about = LinkLabel(self.labels, "color: rgba(0, 0, 0, 60%)", "color: rgba(0, 0, 0, 60%)")
        self.app_about.setText("")
        self.app_about.setFont(QFont("Roboto Light", 11))
        self.app_about.move(self.labels.x() + _margins * 8, self.labels.y() + _margins * 2)

        self.setStyleSheet("background: white;")

    def paintEvent(self, event):
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, p, self)
    
    def button_budget(self):
        print("Hola")

class SideMenu(QMdiSubWindow):
    def __init__(self):
        super(SideMenu, self).__init__()
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(50)
        self.setGraphicsEffect(self.shadow)

        self.widget = SideMenuWidget()
        self.setWidget(self.widget)
        #self.hide()