'treasure map lists'

row1= ["a","b","c"]
row2= ["d","e","f"]
row3= ["g","h","i"]

guide = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

postion = input("Where do you want to put the treasure?")

posx= (int(postion[0]) -1)
posy = (int(postion[1]) -1)

print(f"{posx} {posy}")

guide[posy][posx]="x"

print(f"{row1}\n{row2}\n{row3}")