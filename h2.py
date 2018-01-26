a = input("Enter weight(Kg): ")
b = input("Enter height(m): ")
w = float(a)
h = float(b)
Bmi = w / (h * h)
#判断
if Bmi < 18.5:
    result = "Too light!!!"
elif Bmi >= 18.5 and Bmi < 25:
    result = "Normal"
elif Bmi >= 25 and Bmi <28:
    result = "Too heavy!!!"
elif Bmi >= 28 and Bmi < 32:
    result = "Fat"
elif Bmi >= 32:
    result = "Too fat"
    
print(Bmi, ",", result)

