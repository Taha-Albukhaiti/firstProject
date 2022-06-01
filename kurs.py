import random


""" 
n = random.randint(0, 100)
print("Raten: Geb eine Zahl zwischen 0 und 100: ")

zahl = None
s = 0
while zahl != n:
    zahl = float(input())
    if zahl == n:
        print("Gut geraten")
        break
    elif zahl < n:
        print("Ist kleiner")
        s += 1
    else:
        print("größer")
        s+=1

print(s)
"""
da =  {
    "Skills": {
        "Java": "80%",
        "JavaScript": "40%",
        "HTML": "50%",
        "CSS": "30%",
        "SQL": "65%"
    },
    "Info": {
        "Vorname": "Taha",
        "Nachname": "Al-Bukhaiti",
        "Alter": "24"
    }
}

for s, i in da.items():
    print(f"{s} ")
    for i1, i2 in i.items():
        print(f"- {i1} => {i2}")
