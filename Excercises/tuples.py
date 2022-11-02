'working w/ tuples'

my_tuple=(1,2,3,4,5)

new_tuple=my_tuple[1:3]

x,y,z, *other = (1,2,3,4,5)

print(other)

dict = {
    (1,2): ['meow']
}

print(new_tuple)

print(dict[(1,2)])

print(my_tuple)

print(my_tuple.index(4))