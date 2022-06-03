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
da = {
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


def addition(a, b):
    if type(a) != int or type(b) != int:
        print("So geht es nicht")
    else:
        print(a + b)


addition(2, "e")


def full_name(first, Mittel, last):
    print(f"Hello Mr. {first.strip().capitalize()} {Mittel.upper():.1s} {last.capitalize()}")


full_name("   Taha   ", "Mohammed", "Albukhaiti")


def he(name, *skills):
    print(f"Hello {name} Your Skills are:")
    for skill in skills:
        print(f"{skill}")


he("Taha", "Java", "JS", "HTML", "CSS", "SQL")


def he(name="Unknown"):
    print(f"Hello {name} Your Skills are:")


he()

da1 = {

    "Java": "80%",
    "JavaScript": "40%",
    "HTML": "50%",
    "CSS": "30%",
    "SQL": "65%"
}


def he1(name, **skills):
    print(f"Hello {name} Your Skills are:")
    for skill, value in skills.items():
        print(f"{skill} => {value}")


he1("Taha",
    Java="80%",
    JavaScript="40%",
    HTML="50%",
    CSS="30%",
    SQL="65%")

he1("Taha", **da1)


def show_skills(name, *skills, **skillsWithProgress):
    print(f"Hello {name}\nSkills Without Progress Is:")
    for skill in skills:
        print(f"- {skill}")

    for skill, value in skillsWithProgress.items():
        print(f"- {skill} => {value}")


show_skills("Taha", "SQL", "Java", "JS")
show_skills("Taha", **da1)


def faku(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * faku(n - 1)


print(faku(3))


def cleanWord(word):
    if len(word) == 1:
        return word
    if word[0] == word[1]:
        print(f"befor Condition {word}")
        return cleanWord(word[1:])

    print(f"befor Return {word}")
    return word[0] + cleanWord(word[1:])


print(cleanWord("WWWooorrld"))


def say_hello(name): return f"Hello {name}"


hello1 = lambda name, age: f"Hello {name}, Your age is  {age}"

print(say_hello("Taha"))
print(hello1("Taha", 24))

"""
-- The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.


sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
"""


def sleep_in(weekday, vacation):
    if weekday == False and vacation == False:
        return True
    elif weekday == True and vacation == False:
        return False
    elif weekday == False and vacation == True:
        return True
    else:
        return True


print(sleep_in(False, False))  # → True
sleep_in(True, False)  # → False
sleep_in(False, True)  # → True


def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False
    # This can be shortened to: return(not weekday or vacation)


"""
-We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
-We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
"""


def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return True
    else:
        return False


"""
Given two int values, return their sum. Unless the two values are the same, then return double their sum.


sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
"""


def sum_double(a, b):
    sum = 0
    if a != b:
        return a + b
    else:
        sum = a + b
        return sum * 2


print(sum_double(2, 2))

"""
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.


diff21(19) → 2
diff21(10) → 11
diff21(21) → 0

"""


def diff21(n):
    if n <= 21:
        return 21 - n
    elif n > 21:
        return (n - 21) * 2


"""
We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.


parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False

"""


def parrot_trouble(talking, hour):
    if (talking and hour < 7) or (talking and hour > 20):
        return True
    else:
        return False


def parrot_trouble(talking, hour):
    return (talking and (hour < 7 or hour > 20))
    # Need extra parenthesis around the or clause
    # since and binds more tightly than or.
    # and is like arithmetic *, or is like arithmetic +


"""

Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True
"""


def makes10(a, b):
    if a == 10 or b == 10 or (a + b) == 10:
        return True
    else:
        return False


def makes10(a, b):
    return (a == 10 or b == 10 or a + b == 10)


""" 
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.


near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False

"""


def near_hundred(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))


"""


Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.


pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
"""


def pos_neg(a, b, negative):
    return (((a < 0 and b > 0) or (a > 0 and b < 0)) and negative == False) or ((a < 0 and b < 0) and negative == True)


"""

Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.


not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
"""


def not_string(str):
    if str[0:3] == "not":
        return str
    else:
        return "not " + str


def not_string(str):
    if len(str) >= 3 and str[:3] == "not":
        return str
    return "not " + str
    # str[:3] goes from the start of the string up to but not
    # including index 3


"""
Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).


missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'
"""


def missing_char(str, n):
    return str[:n] + "" + str[n + 1:]


"""

Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""


def front_back(str):
    if len(str) <= 1:
        return str
    return str[len(str) - 1] + str[1:len(str) - 1] + str[0]


"""
Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.


front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'
"""


def front3(str):
    return str[0:3] + str[0:3] + str[0:3]


def array_front9(nums):
    if len(nums) == 0:
        return False

    for i in nums[0:5]:
        if i == 9:
            return True
        else:
            return False
    if len(nums) <= 5:
        for i in nums[0:]:
            if i == 9:
                return True
            else:
                return False


def array_front9(nums):
    end = len(nums)
    if end > 4:
        end = 4
    for i in range(end):  # loop over index [0, 1, 2, 3]
        if nums[i] == 9:
            return True
    return False


