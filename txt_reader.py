import os
from point2d import Point2D
from math import sqrt

input_point = Point2D() 
for filename in dirs:
    if filename.endswith(".txt"):
        print(f'주어진 좌표는{(point.xcoord,point.ycoord)}')
        print("==================================================================")
        print("==================================================================")
        f = open(filename,'r')
        files =f.readlines()
        file_input_point=[file.strip() for file in files]
        for i  in range(len(files)):
            if ',' in file_input_point[i]:
                file_input_point[i] = file_input_point[i].split(',')
                input_point.xcoord = float(file_input_point[i][0])
                input_point.ycoord = float(file_input_point[i][1])
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
        f.close