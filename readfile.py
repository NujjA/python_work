#import os
#cwd = os.getcwd()
#print(cwd)
	
#print(os.listdir(cwd))
filename = "C:/Users/Najla/Documents/python_work/readfile.txt.txt"

with open(filename) as file_object:
    lines = file_object.readlines()
    

for x in range(0,3):
    for line in lines:
        print(line)
