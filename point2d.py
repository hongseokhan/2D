from math import sqrt
class Point2D:
    def __init__(self):
        self.__x = 0.0
        self.__y = 0.0   

    @property
    def xcoord(self):
        return self.__x
    
    @xcoord.setter
    def xcoord(self,x):
        self.__x = x

    @property
    def ycoord(self):
        return self.__y
    
    @ycoord.setter
    def ycoord(self,y):
        self.__y = y

    def get_distance_between_points(self, input_point):
        distance = sqrt(pow(self.xcoord - input_point.xcoord,2) + pow(self.ycoord - input_point.ycoord,2))
        return distance
    
    def shift_points(self,input_point):
        xcoord = self.xcoord + input_point.xcoord
        ycoord = self.ycoord + input_point.ycoord
        return (xcoord,ycoord)
    
    def get_center_between_points(self, input_point):
        xcoord = (self.xcoord+input_point.xcoord)/2.0
        ycoord = (self.ycoord+input_point.ycoord)/2.0
        return (xcoord,ycoord)
    
    def get_gradient_between_points(self, input_point):
        try:
            gradient = (self.xcoord-input_point.xcoord)/(self.ycoord-input_point.ycoord)
            return gradient
        except Exception as e:
            print('예외 발생상황:',e)
    

    def get_ycoord_intercept(self,input_point):
        ycoord_intercept = self.ycoord - input_point.ycoord  
        return ycoord_intercept


    


