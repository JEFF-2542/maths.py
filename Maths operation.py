#Ask for user input
num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ") 

#perform the calculation based on the operation
if operation == "+":
 result =num1 + num2
 print(f"{num1} + {num2} = {result}")
else:
 print("Invalid operation!")