import os
path = "C:\\Users\\tjrgk\\Documents\\GitHub\\2D\\"
dirs =  os.listdir(path)
if 'circle' in dirs:
    path = os.chdir(path+"\\circle")
    dirs =os.listdir(path)
    for filename in dirs:
        print(filename)
        if filename.endswith(".txt"):
            f = open(filename,'r')
            files = f.readlines()
        