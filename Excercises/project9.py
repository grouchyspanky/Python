' finding dups in list'

some_list = ['a', 'b', 'c', 'b', 'd' , 'm' , 'n', 'n']


dups = []
for i in some_list:
    if some_list.count(i) > 1:
        if i not in dups:
            dups.append(i)
        
print(dups)
    