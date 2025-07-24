'''
    write a program to findout person obesity level using BMI technique.
    ---------------------------------------------------------------------
    obesity level 
        Underweight: BMI less than 18.5
        Normal: BMI between 18.5 to 24.9
        Overweight: BMI between 25.0  29.9
        Obese: BMI between 30.0  34.9
        Extremely Obese: BMI 35.0 and above
    steps 
    1) accept weight from user into weight variable (kg)
    2) accept foot from user into foot variable 5
    3) accept inch from user into user variable 7
    4) calculate total inches from given foot and inches 
        inch = inch + (foot * 12)
    5) convert inch into meters 
        meter = inch/39.37
    6) apply formula to calculate bmi 
        bmi = weight / (meter * meter)
    7) display bmi 
    8) calculate & display obesity level 
       8.1 if bmi<18.5 then 
        print person is underweight
       8.2 if bmi>=18.5 and bmi<=24.9  
        print person is normal
       8.3 if bmi>=25.0 and bmi<=29.9
        print person is overweight
       8.4 if bmi>=30.0 and bmi<=34.9
        print person is Obese 
       else 
        print person is Extremely Obese     
'''
weight = float(input("enter your weight in kg"))
print("Enter your height in foot and inches")
foot = int(input("First enter only foot "))
inches = int(input("now enter only remaining inches"))
inches = inches + (foot * 12)
meter = inches / 39.37
bmi = weight / (meter * meter)
print(bmi)
if bmi<18.5:
    print("person is underweight")
elif bmi>=18.5 and bmi<=24.9:
    print("person is normal")
elif bmi>=25.0 and bmi<=29.9:
    print("person is overweight")
elif bmi>=30.4 and bmi<=34.9:
    print("person is Obese")
else:
    print("person is extremely Obese")
