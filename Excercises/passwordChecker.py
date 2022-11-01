'password checker'

userName=input('Enter your name\n')
userPass=input('Enter your password\n')

passlength = len(userPass)

password = '*' * passlength

print(f'{userName} your password, {password} is {passlength} characters long.\n')

checkPas = input('Do you remember your password?\n Enter your password.\n')

if checkPas == userPass:
    print("You remembered your password.\n")

if checkPas != userPass:
    print('You forgot your password already?\n')