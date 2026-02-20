import math
num1 = input("enter the first number :")
operator = input("enter the operation you wish to perfect (+,-,*,/)")
num2 =input ("enter the second number :")

num1 = float(num1)
num2= float(num2)

if operator =="+":
    print(num1+num2)
elif operator =="-":
    print(num1-num2)
elif operator =="*":
    print(num1*num2)  
elif operator == "/" :
    print(num1/num2)  

else:
    print("invalid operator entered")  

print(num1, operator, num2, "=" , print)      


