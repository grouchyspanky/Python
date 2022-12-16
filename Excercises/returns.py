"working with returns"
def sumnum(num1,num2):
    '''
    Info: this function adds two nums together
    '''
    num3 = num1 + num2
    return num3

help(sumnum)

print(sumnum.__doc__)

print(sumnum(5,5))   