import os

""" 
print(os.getcwd())
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
# Change Current Working Directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())
# file = open("taha.txt")
file = open("/Users/tahaalbukhaiti/eclipse/EAs/test.txt")
file = open("files/test1.txt")

print(myFile)
print(myFile.name)
print(myFile.mode)
print(myFile.encoding)

"""

myFile = open("files/taha.txt", "r")
# print(myFile.read())
# print(myFile.readline(10))
print(myFile.readlines())
print(type(myFile.readlines()))

""" 
myfile = open("files/myfile.txt", "w")
myfile = open("files/fun.txt", "w")
myList = ["Taha\n", "Al-Bukhaiti"]
myfile.writelines(myList)
"""
myfile = open("files/myfile.txt", "a")
myList = ["Taha\n", "Al-Bukhaiti"]
#myfile.writelines(myList)
myfile.write("Hello")
