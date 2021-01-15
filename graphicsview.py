import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,QPen, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from ui_graphicsview import Ui_GraphicsviewWindow

class GraphicsviewWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_GraphicsviewWindow()
        self.ui.setupUi(self)
        scene = QGraphicsScene(self)
        greenBrush = QBrush(Qt.green)
        blueBrush = QBrush(Qt.blue)
        blackPen = QPen(Qt.black,5)
        ellipse = scene.addEllipse(1,1,100,100,blackPen,greenBrush)
        self.ui.graphicsView = QGraphicsView(scene)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.show()
