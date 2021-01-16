import os
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,QPen, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from ui_graphicsview import Ui_GraphicsviewWindow
from filereader import Filereader

class GraphicsviewWindow(QMainWindow,Ui_GraphicsviewWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        scene = self.make_figure()
        self.graphicsView.setScene(scene)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def make_figure(self):
        scene = QGraphicsScene()
        blackPen = QPen(Qt.black,0.3)
        blackBrush =QBrush(Qt.black)
        redPen = QPen(Qt.red,0.4)
        #좌표평면
        side = 20
        for i in range(20):
            for j in range(20):
                r = QtCore.QRectF(QtCore.QPointF(i*side, j*side), QtCore.QSizeF(side, side))
                scene.addRect(r, blackPen)
                origin_point_radius = 3
                center = 200
                scene.addEllipse(center-origin_point_radius,center-origin_point_radius,origin_point_radius*2,origin_point_radius*2,blackPen,blackBrush)
        #point 파일 출력
        file = Filereader()
        num = file.get_number_of_circles()
        for i in range(num):
            x,y,radius = file.getcircle(i)
            print(f'Radius is {radius}')
            print(f'center is {x,y}')
            scene.addEllipse(x-radius,y-radius,radius*2,radius*2,redPen)
        #circle 파일 출력
        num = file.get_number_of_points()
        for i in range(num):
            radius = 5
            x,y = file.getpoint(i)
            print(f'Radius is {radius}')
            print(f'center is {x,y}')
            scene.addEllipse(x-radius,y-radius,radius*2,radius*2,redPen)
        return scene


    


