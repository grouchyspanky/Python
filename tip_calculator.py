'tip calculator'

print("Welcome to the tip calculator\n")
total_Bill=input("What was the total bill? $ \n")

tip_Percent= input("What percentage tip would you like to give? 10,12,15 or other?\n")

total_People= input("How many people are going to split the bill?\n")

total_tip = (float(total_Bill) / int(total_People) * ( int(tip_Percent) * .01 + 1) )

print(f"Each person will pay ${round(total_tip,2)}")
