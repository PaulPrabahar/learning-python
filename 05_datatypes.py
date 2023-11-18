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