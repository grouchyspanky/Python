'working with conditions'
is_old = True

is_licenced = False

if is_old and is_licenced:
    print("You are old enough to drive")
elif is_licenced:
    print('You can have no license')    
else:
    print("You are not old enough")
    
is_friend= True

can_message='message allowed' if is_friend else 'not allowed to message'

print(can_message)

if is_licenced == False:
    print('Falseeeeee')
    
    