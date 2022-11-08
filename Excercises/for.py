'working with lists'

secrets = {
    'name': 'meow',
    'age': '20',
    'eats': 'yes',
}

my_list =[1,2,3,4,5,6,7,8,9,10]

counter= 0

for item in my_list:
    counter=item + counter

print(counter)


for item in secrets.keys():
    print(item)

for item in {1,2,3,4,5}:
    print(item)
    