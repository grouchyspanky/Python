'Checks for leap year'

user_Year=int(input("Which year did you want to check?"))

if user_Year % 4 == 0:
    print(f"This pasts the first test. {user_Year} is evenly divisble by four.")