import os
from point2d import Point2D
from circle2d import Circle2D
from line2d import Line2D

class Filereader:
    def __init__(self):
        pass
        
    def getpoint(self,index):
        input_point = Point2D()
        path = "C:\\Users\\tjrgk\\Documents\\GitHub\\2D\\"
        dirs =  os.listdir(path)
        if 'point' in dirs:
            path = os.chdir(path+"\\point")
            dirs =os.listdir(path)
        for filename in dirs:
            if filename.endswith(".txt"):
                print("==================================================================")
                print("==================================================================")
                f = open(filename,'r')
                files = f.readlines()
                file_input_point=[file.strip() for file in files]
                point_list = []
                for i  in range(len(files)):
                    if ',' in file_input_point[i]:
                        file_input_point[i] = file_input_point[i].split(',')
                        input_point.xcoord = float(file_input_point[i][0])
                        input_point.ycoord = float(file_input_point[i][1])
                        point_list.extend([input_point.xcoord,input_point.ycoord])
        n = 2
        result = [point_list[i * n:(i + 1) * n] for i in range((len(point_list) + n - 1) // n )]
        input_point = tuple(result[index])
        return input_point

    def get_number_of_points(self):
        path = "C:\\Users\\tjrgk\\Documents\\GitHub\\2D\\"
        dirs =  os.listdir(path)
        if 'point' in dirs:
            path = os.chdir(path+"\\point")
            dirs =os.listdir(path)
        for filename in dirs:
            if filename.endswith(".txt"):
                f = open(filename,'r')
                files = f.readlines()
                number_of_points=len(files)
        return number_of_points

    def getcircle(self,index):
        input_circle = Circle2D()
        path = "C:\\Users\\tjrgk\\Documents\\GitHub\\2D\\"
        dirs =  os.listdir(path)
        if 'circle' in dirs:
            path = os.chdir(path+"\\circle")
            dirs =os.listdir(path)
            for filename in dirs:
                if filename.endswith(".txt"):
                    print("==================================================================")
                    print("==================================================================")
                    f = open(filename,'r')
                    files = f.readlines()
                    file_input_circle=[file.strip() for file in files]
                    point_list = []
                    for i  in range(len(files)):
                        if ',' in file_input_circle[i]:
                            file_input_circle[i] = file_input_circle[i].split(',')
                            input_circle.xcoord = float(file_input_circle[i][0])
                            input_circle.ycoord = float(file_input_circle[i][1])
                            input_circle.radius = float(file_input_circle[i][2])
                            point_list.extend([input_circle.xcoord,input_circle.ycoord,input_circle.radius])
        n = 3
        result = [point_list[i * n:(i + 1) * n] for i in range((len(point_list) + n - 1) // n )]
        input_circle = tuple(result[index])
        return input_circle

    def get_number_of_circles(self):
        path = "C:\\Users\\tjrgk\\Documents\\GitHub\\2D\\"
        dirs =  os.listdir(path)
        if 'circle' in dirs:
            path = os.chdir(path+"\\circle")
            dirs =os.listdir(path)
            for filename in dirs:
                if filename.endswith(".txt"):
                    f = open(filename,'r')
                    files = f.readlines()
                    number_of_circles=len(files)
        return number_of_circles

    def getline(self,index):
        input_line = Line2D()
        path = "C:\\Users\\tjrgk\\Documents\\GitHub\\2D\\"
        dirs =  os.listdir(path)
        if 'line' in dirs:
            path = os.chdir(path+"\\line")
            dirs =os.listdir(path)
            for filename in dirs:
                if filename.endswith(".txt"):
                    print("==================================================================")
                    print("==================================================================")
                    f = open(filename,'r')
                    files = f.readlines()
                    file_input_line=[file.strip() for file in files]
                    point_list = []
                    for i  in range(len(files)):
                        if ',' in file_input_line[i]:
                            file_input_line[i] = file_input_line[i].split(',')
                            input_line.start_point.xcoord = float(file_input_line[i][0])
                            input_line.start_point.ycoord = float(file_input_line[i][1])
                            input_line.end_point.xcoord = float(file_input_line[i][2])
                            input_line.end_point.ycoord = float(file_input_line[i][3])
                            point_list.extend([input_line.start_point.xcoord,input_line.start_point.ycoord,input_line.end_point.xcoord,input_line.end_point.ycoord])
            n = 4
            result = [point_list[i * n:(i + 1) * n] for i in range((len(point_list) + n - 1) // n )]
            input_line = tuple(result[index])
            return input_line

    def get_number_of_lines(self):
        path = "C:\\Users\\tjrgk\\Documents\\GitHub\\2D\\"
        dirs =  os.listdir(path)
        if 'line' in dirs:
            path = os.chdir(path+"\\line")
            dirs =os.listdir(path)
            for filename in dirs:
                if filename.endswith(".txt"):
                    f = open(filename,'r')
                    files = f.readlines()
                    number_of_lines=len(files)
        return number_of_lines