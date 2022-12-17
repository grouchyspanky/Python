"arguements and keyword arguements"

def super_func(*args):
    print(*args)
    return sum(args)


super_func(1,2,3,4,5)