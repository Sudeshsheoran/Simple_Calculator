def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def multiply_numbers(num1, num2):
    return num1 * num2

def divide_numbers(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Cannot divide by zero."

print("Simple Calculator")
print("-----------------")

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    result = add_numbers(number1, number2)
    operation = "+"
elif choice == 2:
    result = subtract_numbers(number1, number2)
    operation = "-"
elif choice == 3:
    result = multiply_numbers(number1, number2)
    operation = "*"
elif choice == 4:
    result = divide_numbers(number1, number2)
    operation = "/"
else:
    print("Invalid choice!")
    exit()

print(f"\nResult: {number1} {operation} {number2} = {result}")
