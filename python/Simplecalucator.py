num1=int(input("enter the num1 value"))
num2=int(input("Enter the num2 value"))
operator=input("Enter the operator")

if operator=="+":
    print(f"Addtion of 2 numbers is: {num1+num2} ")
elif  operator=="-":
    print(f"Substraction of 2 numbers is :{num1-num2}")
elif operator=="*":
    print(f"Multiplication of 2 numbers is :{num1*num2}")
elif operator =="/":
    print(f"Division of 2 numbers is : {num1/num2}")
else:
    print("Invalid operator")