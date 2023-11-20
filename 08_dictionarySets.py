#dictonary
from os import name


information = {  #literal assignment.
    "name": 'paul',
    "age": 32,
    "area":True
}

informaton1 = dict(name = 'puppy', age = 22, area = False )  #using constructor function
information2 = dict(name = 'puppy', age = 22, area = False )  #using constructor function

# print(information)
# print(informaton1)

#Accessing the dictionary
print(information["name"]) #using bracket notation.
print(informaton1.get("name"))  #using get method.

# Access all keys in dictionary
print(information.keys()) # to get all available keys

#Accessing all values in the dictionary
print(informaton1.values()) # to get all values in the dictionary

# getting all the key and values as a tuple
print(information.items()) #display all the keys and values a tuple

#verify a key is present
print("name" in information )

#change values
information["name"] = 'Paul'  #literal assignment
informaton1.update({'name':'Prabahar'}) #Using update
informaton1.update({'color':'brown'}) 

# print(information)
print(informaton1)

#Remove items
informaton1.pop('color')
print(informaton1)

informaton1.popitem() #remove last item and return them a tuple
print(informaton1)

#deleting and clearing the dictionary
del information2['age']
print(information2)

information2.clear()
print(information2)

del information2

#copy of a dictionary
information3 = information.copy() #using copy method
print(information3)

information4 = dict(information) #using constructor method
print(information4)

#Nested dictionary
player1 = {
    "name": 'luck',
    "height": 5.6
}
player2 = {
    "name": 'dead',
    "height": 5.8
}
team = {
    'player1':player1,
    'player2':player2
}
print(team['player1']['height'])

#sets
num = {1,2,3,4} #literal assignment
num2 = set((1,2,3,4,5)) #constructor function

# 1=True and 0=false
num3 = {1,True,2,3,4,False,0}
print(num3) #output {False, 1, 2, 3, 4}

#We cannot  refer an set with a index position.

#Adding new value
num.add(8)
print(num)

#updating set with another set
num.update(num2)
print(num)

one={1,2,3,4,5}
two={1,2,3,4,5,6,7,8,9,0}

three = one.union(two) #to merge two set and create a new set
print(three) 