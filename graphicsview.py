import os
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,QPen, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from ui_graphicsview import Ui_GraphicsviewWindow
from filereader import Filereader
from convex_hull_graham import Convexhull

num = 10
conv = Convexhull()
conv.coordinate_list = conv.create_points(num)

class GraphicsviewWindow(QMainWindow,Ui_GraphicsviewWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        coordinate_system = self.make_coordinate_system()
        # circle_group = self.make_circle_item()
        # line_group = self.make_line_item()
        random_point_group = self.make_random_point_item(conv)
        convex_hull_line_group = self.make_convex_hull_line_item(conv)
        coordinate_system.addItem(random_point_group)
        coordinate_system.addItem(convex_hull_line_group)
        self.graphicsView.setScene(coordinate_system)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def make_coordinate_system(self):
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
                center =200
                scene.addEllipse(center-origin_point_radius,center-origin_point_radius,origin_point_radius*2,origin_point_radius*2,redPen,blackBrush)
        return scene

    def make_random_point_item(self,conv):
        blackPen = QPen(Qt.black,0.3)
        blackBrush =QBrush(Qt.black)
        redPen = QPen(Qt.red,0.4)
        random_point_group = QGraphicsItemGroup()
        print(conv.coordinate_list)
        for i in range(num):
            radius = 2
            x,y = conv.coordinate_list[i]
            random_point_item = QGraphicsEllipseItem(x-radius,y-radius,radius*2,radius*2)
            random_point_group.addToGroup(random_point_item)
        return random_point_group

    def make_convex_hull_line_item(self,conv):
        blackPen = QPen(Qt.black,0.3)
        blackBrush =QBrush(Qt.black)
        redPen = QPen(Qt.red,0.4)
        convex_hull_item_group = QGraphicsItemGroup()
        conv.get_sorted_by_angel_group_between_points(num)
        convex_hull = conv.graham_scan()
        for i in range(len(convex_hull)-1):
            start_point =convex_hull[i]
            end_point = convex_hull[i+1]
            print(f'start_point is {start_point}')
            print(f'end_point is {end_point}')
            convex_hull_item = QGraphicsLineItem(start_point[0],start_point[1],end_point[0],end_point[1])
            convex_hull_item_group.addToGroup(convex_hull_item)
            if i  == (len(convex_hull)-2):
                start_point =convex_hull[i+1]
                end_point = convex_hull[0]
                print(f'start_point is {start_point}')
                print(f'end_point is {end_point}')
                convex_hull_item = QGraphicsLineItem(start_point[0],start_point[1],end_point[0],end_point[1])
                convex_hull_item_group.addToGroup(convex_hull_item)
        return convex_hull_item_group

            
    def make_circle_item(self):
        file = Filereader()
        blackPen = QPen(Qt.black,0.3)
        blackBrush =QBrush(Qt.black)
        redPen = QPen(Qt.red,0.4)    
        #point 파일 출력
        circle_group = QGraphicsItemGroup()
        num = file.get_number_of_circles()
        for i in range(num):
            x,y,radius = file.getcircle(i)
            print(f'Radius is {radius}')
            print(f'center is {x,y}')
            circle_item = QGraphicsEllipseItem(x-radius,y-radius,radius*2,radius*2)
            circle_group.addToGroup(circle_item)
        #circle 파일 출력
        num = file.get_number_of_points()
        for i in range(num):
            radius = 5
            x,y = file.getpoint(i)
            print(f'Radius is {radius}')
            print(f'center is {x,y}')
            circle_item = QGraphicsEllipseItem(x-radius,y-radius,radius*2,radius*2)
            circle_group.addToGroup(circle_item)
        return circle_group

    def make_line_item(self):
        file = Filereader()
        line_group = QGraphicsItemGroup()
        blackPen = QPen(Qt.black,0.3)
        blackBrush =QBrush(Qt.black)
        redPen = QPen(Qt.red,0.4)    
        #line 파일 츌력
        num = file.get_number_of_lines()
        for i in range(num):
            start_point_xcoord,start_point_ycoord,end_point_xcoord,end_point_ycoord = file.getline(i)
            print(f'start_point is {start_point_xcoord,start_point_ycoord}')
            print(f'end_point is {end_point_xcoord,end_point_ycoord}')
            line_item = QGraphicsLineItem(start_point_xcoord,start_point_ycoord,end_point_xcoord,end_point_ycoord)
            line_group.addToGroup(line_item)
        return line_group
        
    


