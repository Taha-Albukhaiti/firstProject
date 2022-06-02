import random  # einbinden der Bibliothek zur Erzeugung von Zufallszahlen


def spiel():
    min = 1  # kleinstmögliche Zufallszahl
    max = 100  # größtmögliche Zufallszahl

    zufallszahl = random.randint(min, max)  # erzeugt eine Zufallszahl im Bereich von 'min' bis 'max'
    print(zufallszahl)

    zahl = None
    s = 0
    while zahl != zufallszahl:
        zahl = float(input("Geben sie eine Zahl: "))
        if zahl == zufallszahl:
            print("Gut geraten")
            strin = input("Wollen Sie nochmal Spielen? ")
            if strin == "j" or strin == "J":
                spiel()
            else:
                break
        elif zahl < zufallszahl:
            print("Ist kleiner")
            s += 1
        else:
            print("größer")
            s += 1

    print(s)


spiel()
