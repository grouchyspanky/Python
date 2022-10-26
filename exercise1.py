'test using ints,strings, and type conversion'



name= input('Enter in your name\n')

age= input('what year were you born?\n')

relationship= input('Are you in a relationship y/n\n')

if relationship == 'y':
    relay= ('Relationship')

if relationship =='n':
    relay= ('Single')
     
userage = (2022-int(age))

if relationship=='y':
    userinfo = (f'{name} is in a {relay}.\n  {name} is also {userage}')

if relationship =='n':
    userinfo = (f'{name} is {relay}.\n  {name} is also {userage}')

print(userinfo)
