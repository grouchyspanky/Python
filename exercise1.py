'test using ints,strings, and type conversion'



name= input('Enter in your name\n')

age= input('what year were you born?\n')

relationship= input('Are you in a relationship y/n\n')

if relationship == 'y':
    relayInfo= ('Relationship')

if relationship =='n':
    relayInfo= ('Single')
     
userage = (2022-int(age))

if relationship=='y':
    userinfo = (f'{name} is in a {relayInfo}.\n  {name} is also {userage}')

if relationship =='n':
    userinfo = (f'{name} is {relayInfo}.\n  {name} is also {userage}')

print(userinfo)
