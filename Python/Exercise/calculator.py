def calculator():
    print("Welcome to Benz's calculator (*_*)")
    print("Available operations: + , - , * , // , ** , / ")
    print("Type 'done' to exit the program.")
    
    while True:

        num1 = input("Enter the first number (or type 'done' to quit): ")
        if num1.lower() == 'done':
            print("Goodbye!")
            break
        
        operator = input("Enter an operator (+ , - , * , //, ** , / ): ")
        num2 = input("Enter the second number: ")
        
        
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Invalid input. Please enter numeric values for numbers.")
            continue
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '//':
            result = num1 // num2
        elif operator == '**':
            result = num1 ** num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2
        else:
            print("Invalid operator. Please enter one of +, -, *, //,**,/.")
            continue
        

        print(f"The result of {num1} {operator} {num2} is: {result}")


calculator()                                                                                                                                                                                  