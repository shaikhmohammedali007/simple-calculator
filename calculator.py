print("Hello! Welcome to my Python calculator")
print("My first Python project!")

print("===== SIMPLE CALCULATOR =====")

while True:
    num1 = input("Enter first number (or exit): ")

    if num1 == "exit":
        print("Calculator closed!")
        break

    num1 = float(num1)
    num2 = float(input("Enter second number: "))

    print("\nChoose an operation:")
    print("+ Addition")
    print("- Subtraction")
    print("* Multiplication")
    print("/ Division")
    print("% Remainder")
    print("** Power")

    operator = input("Enter your choice: ")

    if operator == "exit":
        print("Calculator closed!")
        break

    if operator == "+":
        print("Result:", num1 + num2)

    elif operator == "-":
        print("Result:", num1 - num2)

    elif operator == "*":
        print("Result:", num1 * num2)

    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            print("Result:", num1 / num2)

    elif operator == "%":
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            print("Remainder:", num1 % num2)

    elif operator == "**":
        print("Result:", num1 ** num2)

    else:
        print("Invalid operator!")