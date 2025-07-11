Height=float(input("Enter the height in centimeters: "))
Weight=float(input("Enter the weight in kg: "))

Height=Height/100
if Height>0 and Weight>0:
    BMI=Weight/Height**2
    print(f"your bmi is {BMI}")

    if BMI<=16:
        print("You are severely underweight.")
    elif BMI<=18.5:
        print("you are underweight.")
    elif BMI<=25:
        print("you have a normal weight.")
    elif BMI<=30:
        print("you are overweight.")
    elif BMI<=35:
        print("you are obese.")
    else:
        print("you are severely obese.")
else:
    print("please enter valid values for Height and Weight.")


