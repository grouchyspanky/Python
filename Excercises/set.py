'working w/ sets'

#my_set = {1,2,3,4,5,5}

#new_set=my_set.copy

#my_set.clear()

#print(my_set)

#print(new_set)

#print(5 in my_set)

#print(set(my_list))

#print(my_set)

my_set = {1,2,3,4,5,6}

your_set = {5,6,7,8,9,10}


#checks for diff values between the two and displays the diff val if they exist of the first set called

#print(my_set.difference(your_set))

#discards the value called

print(my_set.discard(5))

print(my_set)

#updates set w/ the differences between the compared sets exp if they share 4 and 5 set is updated w/ values removed

print(my_set.difference_update(your_set))

print(my_set)

#checks to see if they share values/ intersect

#print(my_set.intersection(your_set))

#checks to see if theyre disjoined exp dont share values

#print(my_set.isdisjoint(your_set))

#combines the two sets and removes dupes

#print(my_set.union(your_set))

#checks to see if called set is sub set inside of called set exp my_set ={4,5} your_set={4,5,6,7} subset will return true

print(my_set.issubset(your_set))

#checks if called set is superset meaning does it have all values of called set

print(my_set.issuperset(your_set))
