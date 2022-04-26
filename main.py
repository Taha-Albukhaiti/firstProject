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

# -----------------
# -- Set Methods --
# -----------------

# difference()
print("=" * 40)
a = {1, 2, 3, 4}
b = {1, 2, 3, "Osama", "Ahmed"}
print(a)
print(a.difference(b))  # a - b
b.difference_update(a)  # c - d
print(a)
print(b)

print("=" * 40)  # Separator

# difference_update()

c = {1, 2, 3, 4}
d = {1, 2, "Osama", "Ahmed"}
print(c)
c.difference_update(d)  # c - d
print(c)

print("=" * 40)  # Separator

# intersection() Durchschnitt Menge

e = {1, 2, 3, 4, "X", "Osama"}
f = {"Osama", "X", 2}
print(e)
print(e.intersection(f))  # e & f
print(e)

print("=" * 40)  # Separator

# intersection_update()

g = {1, 2, 3, 4, "X", "Osama"}
h = {"Osama", "X", 2}
print(g)
g.intersection_update(h)  # g & h
print(g)

print("=" * 40)  # Separator

# symmetric_difference()

i = {1, 2, 3, 4, 5, "X"}
j = {"Osama", "Zero", 1, 2, 4, "X"}
print(i)
print(i.symmetric_difference(j))  # i ^ j
print(i)

print("=" * 40)  # Separator

# symmetric_difference_update()

k = {1, 2, 3, 4, 5, "X"}
l = {"Osama", "Zero", 1, 2, 4, "X"}
print(k)
k.symmetric_difference_update(l)  # k ^ l
print(k)

# -----------------
# -- Set Methods --
# -----------------

# issuperset()

a = {1, 2, 3, 4}
b = {1, 2, 3}
c = {1, 2, 3, 4, 5}

print(a.issuperset(b))  # True
print(a.issuperset(c))  # False

print("=" * 50)

# issubset()

d = {1, 2, 3, 4}
e = {1, 2, 3}
f = {1, 2, 3, 4, 5}

print(d.issubset(e))  # False
print(d.issubset(f))  # True

print("=" * 50)

# isdisjoint()

g = {1, 2, 3, 4}
h = {1, 2, 3}
i = {10, 11, 12}

print(g.isdisjoint(h))  # False
print(g.isdisjoint(i))  # True

# ---------------------------
# -- Dictionary --
# ----------------
# [1] Dict Items Are Enclosed in Curly Braces
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] Dict Is Not Ordered You Access Its Element With Key
# ----------------------------

# Dictionary

user = {
    "name": "Osama",
    "age": 36,
    "country": "Egypt",
    "skills": ["Html", "Css", "JS"],
    "rating": 10.5
}

print(user)
print(user['country'])
print(user.get("country"))

print(user.keys())
print(user.values())

# Two-Dimensional Dictionary

languages = {
    "One": {
        "name": "Html",
        "progress": "80%"
    },
    "Two": {
        "name": "Css",
        "progress": "90%"
    },
    "Three": {
        "name": "Js",
        "progress": "90%"
    }
}

print(languages)
print(languages['One'])
print(languages['Three']['name'])

# Dictionary Length

print(len(languages))
print(len(languages["Two"]))

# Create Dictionary From Variables

frameworkOne = {
    "name": "Vuejs",
    "progress": "80%"
}

frameworkTwo = {
    "name": "ReactJs",
    "progress": "80%"
}

frameworkThree = {
    "name": "Angular",
    "progress": "80%"
}

allFramework = {
    "one": frameworkOne,
    "two": frameworkTwo,
    "three": frameworkThree
}

print(allFramework)

# ------------------------
# -- Dictionary Methods --
# ------------------------

# clear()

user = {
    "name": "Osama"
}
print(user)
user.clear()
print(user)

print("=" * 50)

# update()

member = {
    "name": "Osama"
}
print(member)
member["age"] = 36
print(member)
member.update({"country": "Egypt"})
print(member)

print("=" * 50)

# copy()

main = {
    "name": "Osama"
}

b = main.copy()
print(b)
main.update({"skills": "Fighting"})
print(main)
print(b)

# keys() + values()

print(main.keys())
print(main.values())

# ------------------------
# -- Dictionary Methods --
# ------------------------

# setdefault()

user = {
    "name": "Osama"
}
print(user)
print(user.setdefault("age", 36))
print(user)

print("=" * 40)

# popitem()

member = {
    "name": "Osama",
    "skill": "PS4"
}
print(member)
member.update({"age": 36})
print(member.popitem())

print("=" * 40)

# items()

view = {
    "name": "Osama",
    "skill": "XBox"
}

allItems = view.items()
print(view)
view["age"] = 36

print(allItems)

print("=" * 40)

# fromkeys()

a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')
b = "X"

print(dict.fromkeys(a, b))

# -------------
# -- Boolean --
# -------------
# [1] In Programming You Need to Known Your If Your Code Output is True Or False
# [2] Boolean Values Are The Two Constant Objects False + True.
# ---------------------------------------------------------------

name = " "
print(name.isspace())

print("=" * 50)

print(100 > 200)
print(100 > 100)
print(100 > 90)

print("=" * 50)

# True Values

print(bool("Osama"))
print(bool(100))
print(bool(100.95))
print(bool(True))
print(bool([1, 2, 3, 4, 5]))

print("=" * 50)

# False Values

print(bool(0))
print(bool(""))
print(bool(''))
print(bool([]))
print(bool(False))
print(bool(()))
print(bool({}))
print(bool(None))

# -----------------------
# -- Boolean Operators --
# -----------------------
# and
# or
# not
# -----------------------

age = 36
country = "Egypt"
rank = 10

print(age > 16 and country == "Egypt" and rank > 0)  # True
print(age > 16 and country == "KSA" and rank > 0)  # False

print(age > 40 or country == "KSA" or rank > 20)  # False
print(age > 40 or country == "Egypt" or rank > 20)  # True

print(age > 16)  # True
print(not age > 16)  # Not True = False

# --------------------------
# -- Assignment Operators --
# --------------------------
# =
# +=
# -=
# *=
# /=
# **=
# %=
# //=
# --------------------------

x = 10  # Var One
y = 20  # Var Two

# Var One = Self [Operator] Var Two
# Var One [Operator]= Var Two

# x += y
x -= y

print(x)

# --------------------------
# -- Comparison Operators --
# --------------------------
# [ == ] Equal
# [ != ] Not Equal
# [ > ] Greater Than
# [ < ] Less Than
# [ >= ] Greater Than Or Equal
# [ <= ] Less Than Or Equal
# --------------------------

# Equal + Not Equal

print("#" * 50)

print(100 == 100)
print(100 == 200)
print(100 == 100.00)

print("#" * 50)

print(100 != 100)
print(100 != 200)
print(100 != 100.00)

print("#" * 50)

# Greater Than + Less Than

print(100 > 100)
print(100 > 200)
print(100 > 100.00)
print(100 > 40)

print("#" * 50)

print(100 < 100)
print(100 < 200)
print(100 < 100.00)
print(100 < 40)

print("#" * 50)

# Greater Than Or Equal + Less Than Or Equal

print(100 >= 100)
print(100 >= 200)
print(100 >= 100.00)
print(100 >= 40)

print("#" * 50)

print(100 <= 100)
print(100 <= 200)
print(100 <= 100.00)
print(100 <= 40)

print("#" * 50)

# ---------------------
# -- Type Conversion --
# ----------------------

# str()

a = 10
b = "20"
print(type(a))
print(type(str(a)))
print(type(int(b)))

print("#" * 50)

# tuple()

c = "Osama"  # String
d = [1, 2, 3, 4, 5]  # List
e = {"A", "B", "C"}  # Set
f = {"A": 1, "B": 2}  # Dictionary

print(tuple(c))
print(tuple(d))
print(tuple(e))
print(tuple(f))

# list()

c = "Osama"  # String
d = (1, 2, 3, 4, 5)  # Tuple
e = {"A", "B", "C"}  # Set
f = {"A": 1, "B": 2}  # Dictionary

print(list(c))
print(list(d))
print(list(e))
print(list(f))

print("#" * 50)

# set()

c = "Osama"  # String
d = (1, 2, 3, 4, 5)  # Tuple
e = ["A", "B", "C"]  # List
f = {"A": 1, "B": 2}  # Dictionary

print(set(c))
print(set(d))
print(set(e))
print(set(f))

print("#" * 50)

# dict()

d = (("A", 1), ("B", 2), ("C", 3))  # Tuple
e = [["One", 1], ["Two", 2], ["Three", 3]]  # List

print(dict(d))
print(dict(e))

# ----------------
# -- User Input --
# ----------------
""" 
print("#" * 50)
print()
fName = input('What\'s Is Your First Name?')
print()
mName = input('What\'s Is Your Middle Name?')
print()
lName = input('What\'s Is Your Last Name?')
print()

fName = fName.strip().capitalize() # Strip löscht die leerzeichen
mName = mName.strip().capitalize() # capitalize macht den ersten Buchstabe groß ansonsten klein
#  lName = lName.strip().capitalize()

print(f"Hello {fName} {mName:.1s} {lName.strip().capitalize()} Happy To See You.")
"""

# ---------------------------
# -- Practical Slice Email --
# ---------------------------

""" 
theName = input('What\'s Your Name ?').strip().capitalize()
theEmail = input('What\'s Your Email ?').strip()

theUsername = theEmail[:theEmail.index("@")]
theWebsite = theEmail[theEmail.index("@") + 1:]

print(f"Hello {theName} Your Email Is {theEmail}")
print(f"Your Username Is {theUsername} \nYour Website Is {theWebsite}")

# email = "Osama@elzero.org"
# print(email[:email.index("@")])

"""

# -------------------------------------
# -- Practical Your Age Full Details --
# -------------------------------------

# Input Age
#  age = int(input('What\'s Your Age ? ').strip())

# Get Age in All Time Units
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print('You Lived For:')
print(f"{months} Months.")
print(f"{weeks:,} Weeks.")
print(f"{days:,} Days.")
print(f"{hours:,} Hours.")
print(f"{minutes:,} Minutes.")
print(f"{seconds:,} Seconds.")

# --------------------
# --  Control Flow  --
# -- If, Elif, Else --
# -- Make Decisions --
# --------------------

uName = "Osama"
uCountry = "Kuwait"
cName = "Python Course"
cPrice = 100

if uCountry == "Egypt":

    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}")

elif uCountry == "KSA":

    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 60}")

elif uCountry == "Kuwait":

    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}")

else:

    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}")

    # ---------------
    # -- Nested If --
    # ---------------

    uName = "Osama"
    isStudent = "Yes"
    uCountry = "Egypt"
    cName = "Python Course"
    cPrice = 100

    if uCountry == "Egypt" or uCountry == "KSA" or uCountry == "Qatar":

        if isStudent == "Yes":

            print(f"Hi {uName} Because U R From {uCountry} And Student")
            print(f"The Course \"{cName}\" Price Is: ${cPrice - 90}")

        else:

            print(f"Hi {uName} Because U R From {uCountry}")
            print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}")


    elif uCountry == "Kuwait" or uCountry == "Bahrain":

        print(f"Hi {uName} Because U R From {uCountry}")
        print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}")

    else:

        print(f"Hi {uName} Because U R From {uCountry}")
        print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}")

# ----------------------------------
# -- Ternary Conditional Operator --
# ----------------------------------

country = "A"

if country == "Egypt":
    print(f"The Weather in {country} Is 15")
elif country == "KSA":
    print(f"The Weather in {country} Is 30")
else:
    print("Country is Not in The List")

# Short If

movieRate = 18
age = 18

if age < movieRate:

    print("Movie S Not Good 4U")  # Condition If True

else:

    print("Movie S Good 4U And Happy Watching")  # Condition If False

print("Movie S Not Good 4U" if age < movieRate else "Movie S Good 4U And Happy Watching")

# Condition If True | If Condition | Else | Condition If False


# -------------------------------------------------
# -- Calculate Age Advanced Version and Training --
# -------------------------------------------------

# Write A Very Beautiful Note
print("#" * 80)
print(" You Can Write The First Letter Or Full Name of The Time Unit ".center(80, '#'))
print("#" * 80)
""" 
# Collect Age Data
age = input("Please Write Your Age").strip()

# Collect Time Unit Data
unit = input("Please Choose Time Unit: Months, Weeks, Days ").strip().lower()

# Get Time Units
months = int(age) * 12
weeks = months * 4
days = int(age) * 365

if unit == 'months' or unit == 'm':

  print("You Choosed The Unit Months")
  print(f"You Lived For {months:,} Months.")

elif unit == 'weeks' or unit == 'w':

  print("You Choosed The Unit Weeks")
  print(f"You Lived For {weeks:,} Weeks.")

elif unit == 'days' or unit == 'd':

  print("You Choosed The Unit Days")
  print(f"You Lived For {days:,} Days.")
"""

# --------------------------
# -- Membership Operators --
# --------------------------
# in
# not in
# --------------------------

# String

name = "Osama"
print("s" in name)
print("a" in name)
print("A" in name)

print("#" * 50)

# List

friends = ["Ahmed", "Sayed", "Mahmoud"]
print("Osama" in friends)
print("Sayed" in friends)
print("Mahmoud" not in friends)

print("#" * 50)

# Using In and Not In With Condition

countriesOne = ["Egypt", "KSA", "Kuwait", "Bahrain", "Syria"]
countriesOneDiscount = 80

countriesTwo = ["Italy", "USA"]
countriesTwoDiscount = 50

myCountry = "Italy"

if myCountry in countriesOne:

    print(f"Hello You Have A Discount Equal To ${countriesOneDiscount}")

elif myCountry in countriesTwo:

    print(f"Hello You Have A Discount Equal To ${countriesTwoDiscount}")

else:

    print("You Have No Discount")

# ----------------------------------
# -- Practical Membership Control --
# ----------------------------------
"""
# List Contains Admins
admins = ["Ahmed", "Osama", "Sameh", "Manal", "Rahma", "Mahmoud", "Enas"]

# Login
name = input("Please Type Your Name ").strip().capitalize()

# If Name is In Admin
if name in admins:

    print(f"Hello {name} Welcome Back")

    option = input("Delete Or Update Your Name ?").strip().capitalize()

    # Update Option
    if option == 'Update' or option == 'U':

        theNewName = input("Your New Name Please ").strip().capitalize()

        admins[admins.index(name)] = theNewName

        print("Name Updated.")

        print(admins)

    # Delete Option
    elif option == 'Delete' or option == 'D':

        admins.remove(name)

        print("Name Deleted")

        print(admins)

    # Wrong Option
    else:

        print("Wrong Option Choosed")

else:

    status = input("Not Admin, Add You Y, N ? ").strip().capitalize()

    if status == "Yes" or status == "Y":

        print("You Have Been Added")

        admins.append(name)

        print(admins)

    else:

        print("You Are Not Added.")

"""
# -------------------
# -- Loop => While --
# -------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------

a = 0

while a < 10:
    print(a)

    a += 1

print("Loop is Done")  # True Become False

while False:
    print("Will Not Print")

# ----------------------------
# -- Loop => While Training --
# ----------------------------
# while condition_is_true
#   Code Will Run Until Condition Become False
# -----------------------

myF = ["Os", "Ah", "Ga", "Al", "Ra", "Sa", "Ta", "Ma", "Mo", "Wa"]

# print(len(myF))  # List Length [10]

a = 0

while a < len(myF):  # a < 10

    print(f"#{str(a + 1).zfill(3)} {myF[a]}")

    a += 1  # a = a + 1

else:

    print("All Friends Printed To Screen.")

# print(myF[0])
# print(myF[1])
# print(myF[2])
# print(myF[3])
# print(myF[4])
# print(myF[5])
# print(myF[6])
# print(myF[7])
# print(myF[8])
# print(myF[9])

# ----------------------------
# -- Loop => While Training --
# -- Simple Bookmark Manage --
# ----------------------------
""" 
# Empty List To Fill Later
myFavouriteWebs = []

# Maximum Allowed Websites
maximumWebs = 5

while maximumWebs > 0:

    # Input The New Website
    web = input("Website Name Without https:// ")

    # Add The New Website To The List
    myFavouriteWebs.append(f"https://{web.strip().lower()}")

    # Decrease One Number From Allowed Websites
    maximumWebs -= 1  # maximumWebs = maximumWebs - 1

    # Print The Add Message
    print(f"Website Added, {maximumWebs} Places Left")

    # Print The List
    print(myFavouriteWebs)

else:

    print("Bookmark Is Full, You Cant Add More")

# Check If List Is Not Empty
if len(myFavouriteWebs) > 0:

    # Sort The List
    myFavouriteWebs.sort()

    index = 0

    print("Printing The List Of Websites in Your Bookmark")

    while index < len(myFavouriteWebs):
        print(myFavouriteWebs[index])

        index += 1  # index = index + 1

"""

# ----------------------------
# -- Loop => While Training --
# -- Simple Password Guess --
# ----------------------------

""" 
tries = 4

mainPassword = "Osama@123"

inputPassword = input("Write Your Password: ")

while inputPassword != mainPassword:  # True

  tries -= 1  # tries = tries - 1

  print(f"Wrong Password, { 'Last' if tries == 0 else tries } Chance Left")

  inputPassword = input("Write Your Password: ")

  if tries == 0:

    print("All Tries Is Finished.")

    break

    # print("Will Not Print")

else:

  print("Correct Password")

"""

# -----------------
# -- Loop => For --
# -----------------
# for item in iterable_object :
#   Do Something With Item
# -----------------------------
# item Is A Vairable You Create and Call Whenever You Want
# item refer to the current position and will run and visit all items to the end
# iterable_object => Sequence [ list, tuples, set, dict, string of charcaters, etc ... ]
# ---------------------------------------------------------------

myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in myNumbers:

    # print(number * 17)

    if number % 2 == 0:  # Even

        print(f"The Number {number} Is Even.")

    else:

        print(f"The Number {number} Is Odd.")

else:

    print("The Loop Is Finished")

myName = "Taha"

for letter in myName:
    print(f" [ {letter.upper()} ] ")

# -----------------
# -- Loop => For --
# --  Trainings  --
# -----------------

# Range

myRange = range(1, 101)

for number in myRange:
    print(number)

# Dictionary

mySkills = {
    "Html": "70%",
    "Css": "60%",
    "JS": "60%",
    "Java": "70%",
    "Python": "30%",
    "MySQL": "80%"
}

print(mySkills['JS'])
print(mySkills.get("Python"))

for skill in mySkills:
    # print(skill)

    print(f"My Progress in Lang {skill} Is: {mySkills.get(skill)}")


# -----------------
# -- Loop => For --
# -- Nested Loop --
# -----------------

print("#" * 40)
peoples = ["Osama", "Ahmed", "Sayed", "Ali"]

skills = ['Html', 'Css', 'Js']

for name in peoples:  # Outer Loop

  print(f"{name} Skills Is: ")

  for skill in skills:  # Inner Loop

    print(f"- {skill}")

# Dictionary

peoples = {
  "Osama": {
    "Html": "70%",
    "Css": "80%",
    "Js": "70%"
  },
  "Ahmed": {
    "Html": "90%",
    "Css": "80%",
    "Js": "90%"
  },
  "Max": {
    "Html": "70%",
    "Css": "60%",
    "Js": "90%"
  }
}

print(peoples["Osama"])
print(peoples["Ahmed"])
print(peoples["Max"])

print(peoples["Osama"]['Css'])
print(peoples["Ahmed"]['Css'])
print(peoples["Max"]['Css'])

for name in peoples:

  print(f"Skills and Progress For {name} Is: ")

  for skill in peoples[name]:

    print(f"{skill.upper()} => {peoples[name][skill]}")

print("#" * 50)

# ---------------------------
# -- Break, Continue, Pass --
# ---------------------------

myNumbers = [1, 2, 3, 5, 7, 10, 13, 14, 15, 19]

# Continue

for number in myNumbers:

  if number == 13:

    continue

  print(number)

print("#" * 50)

# Break

for number in myNumbers:

  if number == 13:

    break

  print(number)

print("#" * 50)

# Pass

for number in myNumbers:

  if number == 13:

    pass

  print(number)

print("#" * 60)
# ------------------------------
# -- Advanced Dictionary Loop --
# ------------------------------

mySkills = {
  "HTML": "80%",
  "CSS": "90%",
  "JS": "70%",
  "PHP": "80%"
}

print(mySkills.items())

#######################

for skill in mySkills:

  print(f"{skill} => {mySkills[skill]}")

#######################

for skill_key, skill_progress in mySkills.items():

  print(f"{skill_key} => {skill_progress}")

#######################

myUltimateSkills = {
  "HTML": {
    "Main": "80%",
    "Pugjs": "80%"
  },
  "CSS": {
    "Main": "90%",
    "Sass": "70%"
  }
}

for main_key, main_value in myUltimateSkills.items():

  print(f"{main_key} Progress Is: ")

  for child_key, child_value in main_value.items():

    print(f"- {child_key} => {child_value}")