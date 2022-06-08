"""
In einer Datei ‘studierende.csv’ existiert eine Liste der Studierenden einer Hochschule.
 Gespeichert sind Vorname,
 Nachname und die Matrikelnummer. Gesucht ist eine CSV-Datei ‘studierende_n.csv’,
 in der alle Studierenden gespeichert sind,
 deren Nachname ‘n’ mit einem während der Laufzeit des Programms per Tastatur eingegebenen Buchstaben beginnen.
 Beispielsweise hat eine Datei, in der nur Studierende, deren Nachname mit ‘B’ beginnt, stehen, den Dateinamen
 ‘studierende_b.csv’. – Zur Kontrolle sollen alle Namen der Studierenden auch auf dem Bildschirm dargestellt werden.
 Hinweis: Um einen String ‘zeichenkette’ in Großbuchstaben umzuwandeln,
  lässt sich der Befehl ‘zeichenkette.upper()’ nutzen. Der Befehl ‘zeichenkette.lower()’
  wandelt den String in Kleinbuchstaben um.


"""

from pathlib import Path

""" 
# type(myFile.readlines())
for line in myFile:
    if ";" in line:
        if ";N" in line:
            print(line)
        elif ";B" in line:
            print(line)
"""
"""
from pathlib import Path

myFile = open("files/studierende.csv")

inp = input("Geben Sie Ihre Vorname: ")
inp1 = input("Geben Sie Ihre Nachname und Martikelnummer: ")
mar = input("Geben Sie Ihre Martikelnummer: ")
s = False
for line in inp1:
    if line.upper().startswith("N"):
        myfile = Path('files/studierende_n.csv')
        myfile.touch(exist_ok=True)
        f = myfile.open("a")
        f.write(inp.strip() + ";" + inp1.strip() + ";" + mar+"\n")
        print(myfile.read())

    elif line.upper().startswith("B"):
        myfile = Path('files/studierende_b.csv')
        myfile.touch(exist_ok=True)
        f = myfile.open("a")
        f.write(inp.strip() + ";" + inp1.strip() + ";" + mar+"\n")
        print(myfile.read())


from pathlib import Path

#myFile = open("studierende.csv")

"""

"""
from pathlib import Path

import os

inp = input("Geben Sie Ihre Vorname: ")
inp1 = input("Geben Sie Ihre Nachname: ")
mar = input("Geben Sie Ihre Matrikelnummer: ")
s = False


for line in inp1:
    if line.upper().startswith("N"):
        myfile1 = open('studierende_n.csv', "a+")
        myfile1.write(inp.strip()+ ";" + inp1.strip() + ";" + mar +"\n" )
        myfile1.seek(0)
        print(myfile1.read())
        myfile1.close()
    elif line.upper().startswith("B"):
        myfile2 = open('studierende_b.csv', "a+")
        myfile2.write(inp.strip() + ";" + inp1.strip() + ";" + mar +"\n" )
        myfile2.seek(0)
        print(myfile2.read())
        myfile2.close()

"""

from pathlib import Path

import os

inp = input("Geben Sie Ihre Vorname: ")
inp1 = input("Geben Sie Ihre Nachname: ")
mar = input("Geben Sie Ihre Matrikelnummer: ")
s = False

for line in inp1[0]:
    myfile1 = open('files/studierende_' + line + '.csv', "a+")
    myfile1.write(inp.strip() + ";" + inp1.strip() + ";" + mar + "\n")
    myfile1.seek(0)
    print(myfile1.read())
    myfile1.close()
