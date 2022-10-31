'working with lists in py'

someList = [1,2,2,3,5,4,6,7,8,9]

#append adds num to end of list

someList.append(100)

print(someList)

#first val is index of list $ second is value to insert

someList.insert(0,200)

print(someList)

#remove , removes first instance of value

someList.remove(200)

print(someList)

#pop removes val at that index

someList.pop(9)

print(someList)

#mods list and appends inputted list into called list

someList.extend([300,400])

print(someList)

# in gives bool result true or false if val is in list

print(1 in someList)

#index finds location of value

print(someList.index(400))

#count finds how many times val occurs

print(someList.count(2))

#clear clears list

#someList.clear()

print(someList)

#sorts list by val or alph by making a new list that is sorted

#reverse, reverses the list
someList.reverse()

print(someList)

someList.sort()

print(someList)

print(list(range(100)))