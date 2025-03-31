def basic_calculator():
    """
    A simple calculator program that takes two numbers and an operator as input.
    """
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter the operator (+, -, *, /): ")

        if operator == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operator == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operator == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operator == '/':
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid operator.")

    except ValueError:
        print("Invalid input. Please enter numbers.")

basic_calculator()