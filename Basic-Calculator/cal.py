operator=input("Enter the operate (+,-,*,/) : ")
num1=float(input("Enter the first number : "))
num2=float(input("Enter the secound number : "))
if operator=="+":
    result=num1+num2
    print(f"The Addition of the sum {result}")
elif operator=="-":
    result=num1-num2
    print(f"The Subtraction of the sum {result}")
elif operator=="*":
    result=num1*num2
    print(f"The Multiplication of the sum {result}")
elif operator=="/":
    result=num1/num2
    print(f"The Division of the sum {result}")
else:
    print("Enter a valid symbol!")