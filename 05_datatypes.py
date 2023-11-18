# String data types.
# literal assignment.
first = "paul"
last = "prabahar"
print(type(first))
print(type(first) == str)
print(isinstance(first, str))

#Concatination of a string.
fullname = first +" " + last
print(fullname)

fullname += "!"
print(fullname)

#Casting a number into a string
year = str(2000)
print("I love music from " + year + "...")

#multiline string
multilinestr = '''
hi my name is paul
                  hi i am essaki
hey how are you
                  I am fine.yo.

'''
print(multilinestr)

#Escaping special character
escspel = 'Hey guy\'s \t today i talked to\n essaki.'
print(escspel)

#String methods
print(first.lower())
print(first.upper())
print(first.title())
print(multilinestr.replace("essaki", "femy"))
print(len(multilinestr))
print(len(multilinestr.strip()))
print(len(multilinestr.lstrip()))
print(len(multilinestr.rstrip()))

print("")

#Buliding a menu
tiltle = "menu".upper() #we can use method directly in the value.
print(tiltle.center(20, "*"))
print("coffee".ljust(16, ".") + "$1".rjust(4))
print("tea".ljust(16, ".") + "$1".rjust(4))
print("cake".ljust(16, ".") + "$1".rjust(4))

#string index value
print(first[0])
print(first[0:3])
print(first[0:])

#String methods return boolen data type.
print(first.startswith("p"))
print(first.endswith("l"))

print("")

#Boolean datatypes.
myValue = False
print(type(myValue) == bool )
print(isinstance(myValue, bool))
print("")

#Numeric data type.

#Intger type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(price, int))

#float type
grade = 1.22
best_grade = float(5.33)
print(type(best_grade))

#Complex type
complex = 5+3j
print(type(complex))

#Casting number into a string
pincode = "618005"
print(type(int(pincode)) == int) 