#List
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


