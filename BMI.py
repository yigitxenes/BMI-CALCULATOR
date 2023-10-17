##print("BMI VALUES:")
##print("Underweight: less than 18.5")
##print("Normal: between 18.5 and 24.9")
##print("Overweight: between 25 and 29.9")
##print("Obese: 30 or greater")

weight = int(input("Enter Your Weight in Kilograms: "))
height = float(input("Enter Your Height in Meters: "))
bmi = weight/height**2
if bmi<18.5:
    print("Your BMI is: ", bmi, " You Are Underweight")
elif bmi>=18.5 and bmi<=24.9:
    print("Your BMI is: ", bmi, "You Are Normal")
elif bmi>=25 and bmi<=29.9:
    print("Your BMI is: ", bmi, "You Are Overweight")
else:
    print("Your BMI is: ", bmi, "You Are Obese")
print("BMI VALUES:")
print("Underweight: less than 18.5")
print("Normal: between 18.5 and 24.9")
print("Overweight: between 25 and 29.9")
print("Obese: 30 or greater")
