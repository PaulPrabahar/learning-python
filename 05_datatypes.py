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