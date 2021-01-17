import random
import math
from point2d import Point2D
from line2d import Line2D 

class Convexhull():
    def __init__(self):
        self.__coordinate_list = []

    @property
    def coordinate_list(self):
        return self.__coordinate_list
    @coordinate_list.setter
    def coordinate_list(self,coordinate_list):
        self.__coordinate_list = coordinate_list

    def create_points(self,num):
        for x in range(0,401):
            for y in range(0,401):
                point = (x,y)
                self.__coordinate_list.append(point)
        self.__coordinate_list = random.sample(self.__coordinate_list,num)
        return self.__coordinate_list
    
    def select_lowest_ycoordinate_point(self,num):
        min_y = 401
        min_index = 0
        for index,point in enumerate(self.__coordinate_list):
            if point[1] < min_y:
                min_y = point[1]
                min_index = index
            elif point[1] == min_y:
                if point[0] < self.__coordinate_list[min_index][0]:
                    min_index = index
        return self.__coordinate_list[min_index]

    def get_sorted_by_angel_group_between_points(self,num):
        point_list = []
        angle_list =[]
        ref_start_point = self.select_lowest_ycoordinate_point(num)
        for point in self.__coordinate_list:
            if  point != ref_start_point:
                point_list.append(point)  
        for i in range(len(point_list)):
            dx = self.__coordinate_list[i][1]-ref_start_point[0]
            dy = self.__coordinate_list[i][0]-ref_start_point[1]
            # 각도별로 정렬
            """
            angle = math.degrees((math.atan(dx/dy)))
            if dx < 0.0:
                angle += 180.0
            elif dy<0.0: 
                angle += 360.0
            angle_list.append(angle)
            """
        print(angle_list)
        group = list(zip(angle_list, point_list)) 
        group.sort(key=lambda  x: x[0])
        print(group)
        sorted_coordinate_list =[point_list for angle_list,point_list in group]
        self.__coordinate_list = sorted_coordinate_list
        self.__coordinate_list.insert(0,ref_start_point)
        return self.__coordinate_list

    def cross_product_direction(self,a,b,c):
        """ cross_product_value > 0 (CW)
            cross_product_value < 0 (CCw)
            cross_product_value = 0 (Co-linear)
        """
        return (b[1] -a[1])*(c[0]-a[0]) - (b[0] -a[0])*(c[1]-a[1])

    def graham_scan(self):
        convex_hull = [] # Stack
        for i in self.__coordinate_list:
            while len(convex_hull) > 1 and self.cross_product_direction(convex_hull[-2],convex_hull[-1],i)>= 0:
                convex_hull.pop()
            convex_hull.append(i)
        return convex_hull







