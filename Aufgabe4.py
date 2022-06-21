"""
Gegeben seien die folgenden Daten der fünf nordeutschen Bundesländer (Bundesland: Landeshaupt- stadt, Fläche und Einwohnerzahl):
• Bremen: Bremen, 419,38 km2, 680.130
• Hamburg: Hamburg, 755,09 km2, 1.851.430
• Mecklenburg-Vorpommern: Schwerin, 23.211,25 km2, 1.610.744 • Niedersachsen: Hannover, 47.709,82 km2, 8.003.421
• Schleswig-Holstein: Kiel, 15.804,3 km2, 2.910.875
Ein Programm soll erstellt werden,
1. das im ersten Schritt Bundesländer mit den zugehörigen Daten über die Tastatur einließt. Bundesland für Bundesland.
Soll kein weiteres Bundesland eingegeben werden, wird bei der Abfrage des Bundeslandes ‘-1’ eingegeben.
– Da häufig aus Versehen ein Komma als Dezimaltrennzeichen eingegeben wird,
soll das Programm diese Fehleingabe korrigieren und das Komma durch einen Punkt ersetzen.
2. das im zweiten Schritt alle eingelesenen Daten in einer Textdatei speichert.
Die Daten eines Bundeslandes werden durch Semikolon getrennt in eine Zeile der Datei geschrieben.
Beide Schritte sollen sie getrennt voneinander durchgeführt werden.
Hinweis: Um ein Zeichen in einem String durch ein anderes Zeichen zu ersetzen,
 kann der Befehl replace auf den String angewendet werden, z.B. ersetzt string.replace("x","y")
 alle Vorkom- men von “x” in dem String durch “y”.
"""

"""
def funk(bundsland, hauptstast, flaeche, einwohner):
    bundFile = open("bundesFile.txt", "a+")
    bundFile.write(r"Bundesland:" + bundsland.strip() + ";" + "Hauptstadt:"
                   + hauptstast.strip() + ";" + "Fläche:" + flaeche.strip() + ";" + "Einwohner:"
                   + einwohner.strip() + "\n")
    print(bundFile.read())
    bundFile.close()


while True:
    bundsland = input("Wie heißt Ihre Bunsland? ")
    if bundsland[0:] == "-1":
        break
    hauptstast = input("Wie heißt Ihre Hauptstadt? ")
    flaeche = input("Wie groß ist die Fläsche? ")
    flaeche1 = flaeche.replace(",", ".")
    einwohner = input("Wieviel Einwohner gibt es da? ")
    funk(bundsland, hauptstast, flaeche1, einwohner)
"""
"""
Ein zweites Programm soll die Daten aus der soeben gespeicherten Datei einlesen und sie in einer Tabelle ausgeben.
 In dieser Tabelle soll die Ausgabe wie folgt formatiert sein:
• Die Bundesländer werden zeilenweise dargestellt. In den Spalten der Tabelle finden sich die folgenden Daten:
  Bundesland, Landeshauptstadt, Fläche, Einwohnerzahl, Bevölkerungs- dichte. 
  Die Bevölkerungsdichte berechnet sich als Quotient der Einwohnerzahl durch die Fläche und wird 
  als Ganzzahl dargestellt.
• Bundesländer und Landeshauptstädte werden linksbündig dargestellt, auch in der Spaltenüberschrift.
• Zahlenwerte werden rechtsbündig und Dezimaltrennzeichen werden untereinander dargestellt.
 Zugehörige Spaltenüberschriften werden ebenfalls rechtsbündig dargestellt.
Das Einlesen der Daten und die tabellarische Ausgabe sollen getrennt voneinander durchgeführt werden.

Bundesland             | Hauptstadt |    Fläche | Einwohner | Bevölkerungsdichte
---------------------- | ---------- | --------- | --------- | ------------------
Bremen                 | Bremen     |    419.38 |    680130 |               1621
Hamburg                | Hamburg    |    755.10 |   1851430 |               2451
Mecklenburg-Vorpommern | Schwerin   |  23211.25 |   1610744 |                 69
Niedersachsen          | Hannover   |  47709.82 |   8003421 |                167
Schleswig-Holstein     | Kiel       |  15804.30 |   2910875 |                184
"""


def funk(bundsland, hauptstast, flaeche, einwohner):
    bundFile = open("bundesFile2.txt", "a+")
    bundFile.write(f"- Datensatz" + "\n\n")
    bundFile.write(r"Bundesland: " + bundsland.strip() + "\n" + "Hauptstadt: "
                   + hauptstast.strip() + "\n" + "Fläche    : " + flaeche.strip() + "\n" + "Einwohner : "
                   + einwohner.strip() + "\n\n")
    print(bundFile.read())
    bundFile.close()


while True:
    bundsland = input("Wie heißt Ihre Bunsland? ")
    if bundsland[0:] == "-1":
        break
    hauptstast = input("Wie heißt Ihre Hauptstadt? ")
    flaeche = input("Wie groß ist die Fläsche? ")
    flaeche1 = flaeche.replace(",", ".")
    einwohner = input("Wieviel Einwohner gibt es da? ")
    funk(bundsland, hauptstast, flaeche1, einwohner)

daten = open("bundesFile2.txt", "r")
daten2 = daten.read().split(":", ";")
for zeilen in daten2:
    # print(zeilen[11:zeilen.find(";")])
    print(zeilen)
    if zeilen != "Bundesland":
        # bundes = zeilen[0:zeilen.find(";")]
        print(zeilen)
    # print(zeilen)

daten.close()
