import os
from point2d import Point2D
from math import sqrt

path = "C:\\Users\\ghdtj\\Documents\\GitHub\\2D"
dirs = os.listdir(path)
input_point = Point2D()
point = Point2D()
point.xcoord = 0
point.ycoord = 0
for filename in dirs:
    if filename.endswith(".txt"):
        print(f'주어진 좌표는{(input_point.xcoord,input_point.ycoord)}')
        input_point = Point2D()
        f = open(filename,'r')
        read_input_point = f.readlines()
        print(read_input_point)
        delimiter = [',',' ',':']
    if delimiter in read_input_point:
        read_input_point = read_input_point.split(delimiter)
        input_point.xcoord = float(read_input_point[0])
        input_point.ycoord = float(read_input_point[1])
        print(f'입력된 좌표는 {(input_point.xcoord,input_point.ycoord)}')

        distance  = point.calculate_distance_between_points(input_point)
        print(f'거리는:{distance}')
        
        shifted_points = point.shift_points(input_point)
        print(f'이동된 점은: {shifted_points}')

        center_points = point.calculate_center_between_points(input_point)
        print(f'중점은: {center_points}')

        gradient = point.calculate_gradient_between_points(input_point)
        print(f'기울기는{gradient}')

        straight_line_equation = point.calculate_straight_line_equation(input_point)
        print(straight_line_equation)
        print(f'직선의 방정식은 :y={straight_line_equation[0]}x+{straight_line_equation[1]}')
        print('====================================================================')
        print('====================================================================')
        f.close()