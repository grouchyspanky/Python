'bmi calculator 2'


height = float(input("Enter your height in m: \n"))
weight = float(input("Enter your weight in kg: \n"))

bmi = (weight / (height * height))

print(bmi)

if bmi < 18.5:
    print(f"Your BMI is {round(bmi, 2)}.You are underweight.\n")
elif bmi >= 25 and bmi < 25:
    print(f"Your bmi is {round(bmi,2)}. You are at a normal weight\n")
elif bmi > 25 and bmi < 30:
    print(f"Your bmi is {round(bmi,2)}. You are at a overweight\n")
elif bmi >= 30 and bmi < 35:
    print(f"Your bmi is {round(bmi,2)}. You are obese.\n")
elif bmi >= 35:
    print(f"Your bmi is {round(bmi,2)}. You are clinically obese.\n")
 