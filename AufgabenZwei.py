"""
Nach dem Gregorianischen Kalender dauert ein Jahr exakt 365.2425 Tage, d.h. nicht genau 365 Tage.
Deshalb hat man Schaltjahre eingeführt: - Die ganzzahlig durch vier teilbaren Jahre sind Schaltjahre.
- Die ganzzahlig durch 100 teilbaren Jahre sind jedoch keine Schaltjahre.
 - Die ganzzahlig durch 400 teilbaren Jahre sind wiederum Schaltjahre.
Mithilfe dieser Vorgaben ergibt sich erst nach 3225 Jahren eine Abweichung von einem Tag zum sog.
tropischen Jahr. Schreibe einen Python-Code, der berechnet,
ob ein Jahr ein Schaltjahr ist und prüfe es mit den Jahreszahlen 1875, 1640, 1900, 1925, 1966, 1996, 2000 und 2022.

"""

year = [1875, 1640, 1900, 1925, 1966, 1996, 2000, 2022]
print(year)

for year2 in year:
    if (year2 % 4 == 0) and (year2 % 100 != 0 or year2 % 400 == 0):
        print(year2, " ist ein Schlatjahr")
    else:
        print(year2, " ist nicht Schaltjahr")

"""
Betrachten wir einen Frosch, der einen 2.5 Meter breiten Weg überqueren möchte. Dieser Frosch
ist schon alt und ihn verlassen schnell seine Kräfte: Mit dem ersten Sprung legt er einen Meter
zurück. Mit jedem weiteren Sprung springt er nur noch halb so weit wie vorher. – Die Entfernung,
die der Frosch zurücklegt entspricht also der Summe 1+0.5+0.25+0.125+…
Schreibe einen Python-Code, der nach jedem Sprung ausgibt, wie weit der Frosch insgesamt gekommen ist.

"""
# Nummer des aktuellen Sprungs
sprungnummer = 0
# Insgesamt gesprungene Distanz
distanz = 0  # insgesamt gesprungene Distanz
# Weite des aktuellen Sprungs: Wert muss größer als das Abbruchkriterium sein
aktuelle_sprungweite = 1
# Abbruchkriterium: Sprungweite unter 1 mm
delta = 0.001
# solange die Weite des aktuellen Sprungs größer als 1 mm ist:
while aktuelle_sprungweite > delta:
# Ausgabe der aktuellen Sprungnummer und der insgesamt gesprungenen Distanz
      print("Sprung ",sprungnummer," aktuelle Distanz:",distanz)
# Die Weite des aktuellen Sprungs bestimmen
      aktuelle_sprungweite = 1 / 2 ** sprungnummer
# Die Summe aller Sprünge bestimmen
      distanz += aktuelle_sprungweite
# Die Nummer des aktuellen Sprungs um 1 erhöhen
      sprungnummer += 1
