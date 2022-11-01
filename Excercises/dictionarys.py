#learning about dictionarys in python

'working in dictionarys and lists'


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

print(My_list[1]['b'])
print(My_list[1]['a'][2])

print(dictionary['a'][2])


print('MeowMeow' in My_list)

user2 =dict(name='MeowMeow')

print(user2)

print(dictionary.get('cat_age', 100))

print('x' in dictionary.keys())

print(dictionary.items())

print(dictionary.pop('a'))

print(dictionary.items())

print(dictionary.update({'b': 'Pumpkin'}))

print(dictionary['b'])

print(dictionary.clear)