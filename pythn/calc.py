print("Select the oparation you want to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

operation = int(input())

if operation == 1:
    ##Addition
    num1 = input ("Enter the first number:")
    num2 = input ("Enter the second number:")
    print("The sum of the two numbers is:" + str(int(num1) + int(num2)))
elif operation == 2:
    ##Subtraction
    num1 = input ("Enter the first number:")
    num2 = input ("Enter the second number:")
    print("The outocme of the two numbers is:" + str(int(num1) - int(num2)))
elif operation == 3:
    ##Multiplication
    num1 = input ("Enter the first number:")
    num2 = input ("Enter the second number:")
    print("The output of the two numbers is:" + str(int(num1) * int(num2)))
elif operation == 4:
    ##Division
    num1 = input ("Enter the first number:")
    num2 = input ("Enter the second number:")
    print("The reminder of the two numbers is:" + str(int(num1) / int(num2)))
else:
    print("Invalid input")