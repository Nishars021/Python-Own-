#Weight in kg
weight_kg = 52

#Height in m
height_m = 151

#Calculate BMI
BMI = weight_kg / (height_m ** 2)

#Display BMI 
print("BMI : ",BMI)

#Adult BMI Category
if weight_kg < 18.5 : 
    print("Underweight")

if weight_kg > 18.5 and weight_kg < 24.9 :
    print("Healthy weight")

if weight_kg >= 25 and weight_kg < 29.9 :
    print("Overweight")

if weight_kg > 30 : 
    print("Obesity")

