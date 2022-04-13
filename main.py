"""
This is Not Multiple Line Comments
"""

# ------------------------------
# type()
# All Data in Python is Object
# ------------------------------

print(type(10))  # int => Integer
print(type(-100))  # int => Integer
print(type(100.9))  # float => Floating
print(type("Hallo"))  # String
print(type([1, 2, 3]))  # list
print(type((1, 2, 4)))  # Tupel
print(type({"One": 1, "Tow": 2}))  # dict => Dictionary
print({"One": 1, "Tow": 2})  # dict => Dictionary
print(type(2 == 2))  # bool

# ------------------------------
# -- Variables --
# Syntax => [Variable Name] [Assignment Operator] [Value]
# 1_ Can Start With (a-z A-Z) Or Underscore
# 2- Can't Start With Num Or Special Characters
# Case Sensitive
# ------------------------------

myVariable = "My Value"
print(myVariable)

x = 20
x = "Hallo"
print(x)
help("keywords")

a, b, c = 1, 2, 3

print(a)
print(b)
print(c)

# -------------------------------------------
# Escape Sequences Characters
# \b => Back Space
# \newline => Escape New Line +\
#
# -------------------------------------------

print("Hallo\bTaha")
print("Hello \
I Love \
Python")

print("I Love Back Slash \\")
print('I Love Back Slash \'Test\'')
print("I Love Back Slash \'Test\'")
print("Hello World\nSoso")
print("123456\rAbcd")
print("bcd\tAsfafaf")

print("\x4F")

# -------------------------------------------
# -- Concatenation
# -------------------------------------------

msg = "I Love"
lang = "Python"
print(msg + " " + lang)

full = msg + " " + lang
print(full)

a = "First \
Second \
Third"

b = "A \
B \
C"

print(a + " " + b)
print(a + "\n " + b)

# --------------------------------------------
# -- Strings --
# --------------------------------------------
myS = "This is Double Quote"
myS2 = 'This is Single Quote'
myS3 = "This is Single Qute 'Test'"
print(myS3)

myS4 = """ First 
Secound "Test"
Third
"""
print(myS4)

# --------------------------------------------
# -- Strings --
# --------------------------------------------
# Access Single Item
myS5 = "   This is Double Quote    "
print(myS5[-2])
print(myS5[2])

# Slicing ( Access Multiple Sequence Items )
print(myS5[5:7])
print(myS5[:7])
print(myS5[:])  # Full Data
print(myS5[0::1])  # Full Data
print(myS5[::1])  # Full Data
print(myS5[::2])  #
print(myS5[-1:-6])

print(len(myS5))  # Length
print(myS5.strip())
print(myS5.rstrip())  # links
print(len(myS5.lstrip()))  # links

bestimmtesZeichen = "####Hello######"
print(bestimmtesZeichen.strip("#"))
print(bestimmtesZeichen.lstrip("#"))
print(bestimmtesZeichen.rstrip("#"))

na = "2e sasda 3a"
print(na.title())

na = "2E sasda 3a"
print(na.capitalize())

n, nn, nnn = "1", "21", "111"
print(n)
print(nn)
print(nnn)

print(n.zfill(3))
print(nn.zfill(3))
print(nnn.zfill(3))

# upper()

g = "Taha"
print(g.upper())

g = "Taha"
print(g.lower())

# split() rsplit()
a = " Hallo Lolo "
print(a.split())

a = " Hallo-Lolo "
print(a.split())

a = " Hallo-Lolo "
print(a.split("-"))

a = " Hallo-Lolo-sdasd-sdad "
print(a.split("-", 2))

a = " Hallo-Lolo-sdasd-sdad "
print(a.rsplit("-", 2))

# center()

e = "Taha"
print(e.center(10))
print(e.center(7, "*"))

# count()

f = "Ifas ffasf aksf PHP sda SQL and PHP"
print(f.count("PHP"))
print(f.count("PHP", 0, 22))
print(f.count("PHP", 0))

# swapcase()

f = "SQL and PHP"
print(f.swapcase())
print(f.swapcase())

# startswith()
f = "SQL and PHP"
print(f.startswith("S"))
print(f.startswith("S"))
print(f.startswith("P", 8))
print(f.endswith("P"))

# index()
# index(Substring, Start, ENd)

f = "SQL and PHP"
print(f.index("a", 0, 9))

# find(Substring, Start, ENd)

f = "SQL and PHP"
print(f.find("a", 0, 7))
print(f.find("a", 0, 3))

# rjust(width, File Char) ljust(width, File Char)

m = "Taha"
print(m.rjust(6, "H"))
print(m.rjust(8))
m = "Taha"
print(m.ljust(6, "H"))

# splitlines()

e = """First Line
Srcond Line
Third Line"""
print(e.splitlines())

# expandtabs()

g = "Hello\tWorld\tHier\tist\tTaha"
print(g)
print(g.expandtabs(1))

# Sterings Formating
name2 = "Taha"
age2 = 24
print('Ich bin: %s und bin: %d' % (name2, age2) + " Jahre Alt")
print('Ich bin: {} und bin: {}'.format(name2, age2) + " Jahre Alt")
print('Ich bin: {} und bin: {:.3f}'.format(name2, age2) + " Jahre Alt")

# Numbers Complex
complex = 5 + 6j
print(type(5 + 6j))
print("Real Part Is: {}".format(complex))
print("Real Part Is: {}".format(complex.real))
print("Real Part Is: {}".format(complex.imag))

# Tuples

myTuple = ("Taha", "Ali")
myTuple2 = "Taha", "Ali"
print(myTuple)
print(myTuple2)

# Tuple indxing

mxx = (1, 3, 4, 4, 5)
print(mxx[2])

# Tuple items

mxx = (1, 3, 4, 4, 5, "Taha", True)
print(mxx[-1])

# Tuple with One Element

mxxx = ("Taha",)
print(type(mxxx))
print(len(mxxx))

# Tuple Concatenation

a = (1, 2, 4)
b = (2, 44)
c = a + ("asf", False) + b
print(c)
print(a * 5)

# Methods => count() => index

a = (1, 3, 3, 4, 2, 3, 4, 9, 3)
print(a.count(3))
print("the Position  of Index  Is: {:d}".format(a.index(9)))
print(f"the Position  of Index  Is: {a.index(9)}")

# Tuple Destruct

a = ("A", "B", "C")

# x, y, z = "A", "B", "C"
x, y, z = a
print(x)
print(y)
print(z)

a = ("A", "B", 4, "C")
x, y, _, z = a
print(x)
print(y)
print(z)

# set
m = {"Taha", 23, 42.3, True, (2, 4, 5)}
print(m)
# m = {"Taha", 23, 42.3, True, [2, 4, 5]}  # unhashable type: 'list'

# Items Is Unique Menge keine wiederholung von Elementen

a = {"Taha", "Taha", 3, 4, 3}

print(a)