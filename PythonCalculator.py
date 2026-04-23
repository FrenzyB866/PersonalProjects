#Python calculator

operator = input("Please enter an operator (+ - * /): ")

while operator not in ["+", "-", "*", "/"]:
    print(f"Please enter a valid operator. {operator} is not valid")
    operator = input("Please enter an operator (+ - * /): ")

num1 = float(input("Please enter the 1st number: "))
num2 = float(input("Please enter the 2nd number: "))
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2

print(round(result,3))




