def calculator():
    print("=== Simple Calculator ===")
    print("Available operations: +, -, *, /")
    print()
    
    try:
        # Get input from user
        num1 = float(input("45: "))
        num2 = float(input("34: "))
        operation = input("- (+, -, *, /): ").strip()
        
        # Perform calculation based on operation
        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed!")
        else:
            print("Error: Invalid operation! Please use +, -, *, or /")
    
    except ValueError:
        print("Error: Please enter valid numbers!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the calculator
if __name__ == "__main__":
    calculator()