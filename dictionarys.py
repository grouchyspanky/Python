#learning about dictionarys in python

dictionary = {
    'a': [1,2,3],
    'b': 'Meow',
    'x': True
}

#first item in array is index zero ex, [0][b] = Meow & [1][b] = kitties 

My_list = [
    {
    'a': [1,2,3],
    'b': 'Meow',
    'x': True
    },
    {
    'a': [1,2,6],
    'b': 'kitties',
    'x': True
    },

]

#print(My_list[1]['b'])
#print(My_list[1]['a'][2])
#print(dictionary['a'][2])

user2 =dict(name='MeowMeow')

print(user2)

#print(dictionary.get('cat_age', 100))
