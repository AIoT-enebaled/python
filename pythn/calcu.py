# Define a function for arithmetic operations
def arithmetic_operation():
    # Display a menu of available operations
    print("Select the operation you want to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    # Get the user's choice of operation
    operation = int(input())
    
    # Check the user's choice and perform the corresponding operation
    if operation == 1:
        ##Addition
        # Get two numbers from the user and add them together
        num1 = input("Enter the first number:")
        num2 = input("Enter the second number:")
        print("The sum of the two numbers is:" + str(int(num1) + int(num2)))
    elif operation == 2:
        ##Subtraction
        # Get two numbers from the user and subtract the second one from the first one
        num1 = input("Enter the first number:")
        num2 = input("Enter the second number:")
        print("The outcome of the two numbers is:" + str(int(num1) - int(num2)))
    elif operation == 3:
        ##Multiplication
        # Get two numbers from the user and multiply them together
        num1 = input("Enter the first number:")
        num2 = input("Enter the second number:")
        print("The output of the two numbers is:" + str(int(num1) * int(num2)))
    elif operation == 4:
        ##Division
        # Get two numbers from the user and divide the first one by the second one
        num1 = input("Enter the first number:")
        num2 = input("Enter the second number:")
        print("The reminder of the two numbers is:" + str(int(num1) / int(num2)))
    else:
        # The user entered an invalid choice
        print("Invalid input")

# Call the arithmetic_operation function to start the program
arithmetic_operation()
