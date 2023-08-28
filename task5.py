def calculator():
    # Get the input from the user.
    num1 = float(input("10: "))
    num2 = float(input("5: "))
    operator = input("Enter operator (+, -, *, /): ")
    # Perform the operation.
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        print("Invalid operator.")
        return
    # Print the result.
    print("Result:", result)
# Run the calculator.
calculator()



 
