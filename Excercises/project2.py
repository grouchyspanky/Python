'BMI Calculator'

height = input("Enter your height in m:\n")
weight = input ("Enter your weight in kg:\n")

user_BMI =(float(weight) / (float(height) * float(height)))

print(int(user_BMI))