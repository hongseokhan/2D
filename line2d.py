from math import sqrt
from point2d import Point2D

class Line2D(Point2D):
    def __init__(self):
        self.__start_point = Point2D()
        self.__end_point =  Point2D()
    
    @property
    def start_point(self):
        return self.__start_point

    @start_point.setter
    def start_point(self,start_point):
        self.__start_point =start_point
    
    @property
    def end_point(self):
        return self.__end_point
        
    @end_point.setter
    def end_point(self,end_point):
        self.__end_point =end_point

    def length(self):
        length = self.start_point.get_distance_between_points(self.end_point)
        return length

    def get_intersection_point_between_lines(self,input_line):
        first_gradient_of_line = self.start_point.get_gradient_between_points(self.end_point)
        second_gradient_of_line = input_line.start_point.get_gradient_between_points(input_line.end_point)
        first_ycoord_intercept_of_line = self.start_point.get_ycoord_intercept(self.end_point)
        second_ycoord_intercept_of_line = input_line.start_point.get_ycoord_intercept(input_line.end_point)
        if first_gradient_of_line == second_gradient_of_line:
            print("두직선은 평행합니다")
            return 0
        else:
            intersection_point = Point2D()
            intersection_point.xcoord = ((second_ycoord_intercept_of_line-first_ycoord_intercept_of_line)/(first_gradient_of_line-second_gradient_of_line))
            intersection_point.ycoord =first_gradient_of_line*intersection_point.xcoord+first_ycoord_intercept_of_line
            return intersection_point


# line = Line2D()
# line.start_point.xcoord = 0
# line.start_point.ycoord = 1
# line.end_point.xcoord =3
# line.end_point.ycoord = 2
# input_line = Line2D()
# input_line.start_point.xcoord = 1
# input_line.start_point.ycoord = 1
# input_line.end_point.xcoord =5
# input_line.end_point.ycoord = 5
# interscection_point = line.get_intersection_point_between_lines(input_line)
# print((interscection_point.xcoord,interscection_point.ycoord))
