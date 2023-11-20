#List

myNewList = list([1,1,2,3,5,8,13])
names = ['paul', 'jerry', 'alwin','elbin', 'cyril','Anto','Zaiul','Nanako']
list1 = ["stewie", 11, False]
list = ['paul', 23, True] #list example.
emptylist = [] #empty list example.

print(23 in list)
print(list[0])


print(list.index(23))
print(list[0:3])

print(len(list))
list.append("stewie")
print(list)

list.extend(list1)
print(list)
list.extend(['peter'])
print(list)

list.insert(0, "puppy")
print(list)
# list[0:0] = ["prasanna"] #To replace the element in the particular position but do not remove. 
# print(list)
print(list)
list[0:1] = ["prasanna"]  #To remove and replace the element form a particular index position.
print(list)

list.remove('prasanna')
print(list)

namey = list.pop()
print(list)
print(namey)

del list[3]
print(list)

# list.clear()
# print(list)

# names.sort()
# print(names)

# names.sort(key=str.lower) #the items get sorted irrespective of their case. 
# print(names)

#To make a copy without altering the original list.
#method 1 to use global method.
print(sorted(names))
#method2 to use copy method.
myNames = names.copy()
myNames.sort(key=str.lower)
print(names)
print(myNames)
print(myNewList)

#tuples
myTuple = tuple((1,1,2,3,5,8))
myNewTuple = (1,1,2,5,8,13,21)

(one, anotherone, *remaining) = myNewTuple #unpacking a tuple 
print(one)
print(anotherone)
print(remaining)

#modifying a tuple
modify = list(myNewTuple) #convert to list
modify.append(34) #modify it
modified = tuple(modify) #convert to tuple
print(modified)


