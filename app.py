##Calculator
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
operation = input("Enter operation symbol (+, -, *, /, %, //, **): ")

if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    result = a / b
elif operation == '%':
    result = a % b
elif operation == '//':
    result = a // b
elif operation == '**':
    result = a ** b
else:
    result = "Invalid operator"

print(f"{a} {operation} {b} = {result}")


## palindrome number

num = int(input("Enter a number: "))
if str(num) == str(num)[::-1]:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")


## amstrong number

num = int(input("Enter a number: "))

# Convert number to string to get number of digits
num_str = str(num)
num_digits = len(num_str)

# Calculate sum of digits raised to the power of number of digits
total = sum(int(digit) ** num_digits for digit in num_str)

# Check if the number is an Armstrong number
if total == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
