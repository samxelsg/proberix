def calculator():
    print("Simple Calculator")
    print("Options: +, -, *, /, or 'exit' to quit")

    while True:
        operation = input("\nEnter operation (+, -, *, /) or 'exit' to quit: ").strip()

        if operation == 'exit':
            print("Goodbye!")
            break

        if operation in ['+', '-', '*', '/']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if operation == '+':
                    print(f"{num1} + {num2} = {num1 + num2}")
                elif operation == '-':
                    print(f"{num1} - {num2} = {num1 - num2}")
                elif operation == '*':
                    print(f"{num1} * {num2} = {num1 * num2}")
                elif operation == '/':
                    if num2 != 0:
                        print(f"{num1} / {num2} = {num1 / num2}")
                    else:
                        print("Error: Division by zero is not allowed.")
            except ValueError:
                print("Invalid input! Please enter numerical values.")
        else:
            print("Invalid operation! Please try again.")

if __name__ == "__main__":
    calculator()
