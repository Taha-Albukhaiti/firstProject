
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
print(myS5[:])     # Full Data
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
print(g.lower() )