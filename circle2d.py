from math import sqrt
from point2d import Point2D

class Circle2D(Point2D):
    def __init__(self):
        super().__init__()
        self.__radius = 0

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self,radius):
        self.__radius = radius

    def get_area(self):
        area = math.pi**(self.radius**2)
        return area

    def get_perimeter(self):
        perimeter = 2*math.pi*self.radius
        return perimeter

    def is_contain_between_circle(self,input_circle):
        distance_between_center = self.get_distance_between_points(input_circle)
        if distance_between_center < abs(self.radius-input_circle.radius):
            return True
        else:
            return False
    def is_external_meet_between_circle(self,input_circle):
        distance_between_center = self.get_distance_between_points(input_circle)
        if distance_between_center == self.radius+input_circle.radius:
            return True
        else:
            return False
    def is_internal_meet_between_circle(self,input_circle):
        distance_between_center = self.get_distance_between_points(input_circle)
        if distance_between_center == abs(self.radius-input_circle.radius):
            return True
        else:
            return False

