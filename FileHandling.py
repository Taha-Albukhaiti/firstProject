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
""" 
myFile = open("files/taha.txt", "r")
# print(myFile.read())
# print(myFile.readline(10))
print(myFile.readlines())
print(type(myFile.readlines()))
"""
""" 
myfile = open("files/myfile.txt", "w")
myfile = open("files/fun.txt", "w")
myList = ["Taha\n", "Al-Bukhaiti"]
myfile.writelines(myList)
"""

""" 
myfile = open("files/myfile.txt", "a")
myList = ["Taha\n", "Al-Bukhaiti"]
# myfile.writelines(myList)
myfile.write("Hello")
myfile.close()

datei = open("staedte.txt", "r+")
datei1 = open("großeStaedte.txt", "r+")
zeile = 0
for lesen in datei:
    daten = lesen.strip().split(";")
    if int(daten[1]) < 1000000:
        break
    print(daten)
    zeile += 1
    datei1.write(lesen.strip() + "\n")

datei.close()
datei1.close()

print("Holla")

datei1 = open("großeStaedte.txt", "r+")
for lese in datei1:
    print(lese)
datei1.close()
"""
zahl = 0
with open("staedte.txt", "r") as datei, open("großeStaedte.txt", "w") as datei1:
    for zeile in datei:
        zahl += 1
        daten = zeile.strip().split(";")
        if int(daten[1]) > 1000000:
            datei1.write(str(zahl) + " " + zeile.strip() + "\n")

count = 0
daten = []
with open("staedte.txt", "r") as file:
    for line in file:
        count += 1
        data = line.strip().split(";")
        if count == 10:
            break
for i in range(4):
    print(f"{daten[0][0]:<22} | {daten[0][1]:<10} | {daten[0][2]:>9} | Bevölkerungsdichte")
    print("---------------------- | ---------- | --------- | --------- | ------------------")

    print(f"{data[0]:<22} | {data[1]:<10} | {data[2]:>9}")
