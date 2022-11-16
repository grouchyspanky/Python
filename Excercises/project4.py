'Checks for leap year'

user_Year=int(input("Which year did you want to check?"))

if user_Year % 4 == 0:
    print(f"This pasts the first test. {user_Year} is evenly divisble by four.\n")
    if user_Year % 100 == 0:
        print(f"This past the second test. {user_Year} is evenly divisble by 100.\n")
        if user_Year % 400 == 0:
            print(f"This past the last test. {user_Year} is evenly divisble by 400. Leap Year!\n")
        else:
            print(f"This failed the last test.{user_Year} is not evenly divisible by 400.\n")
    else:
        print(f"This past the second test.{user_Year} is not divisble by 100.Leap year!\n")
else:
    print(f"This fail the first test.{user_Year} is not evenly divisble by four.\n")
        
