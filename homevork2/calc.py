
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
math_action = input("Choose arithmetic operation \n + to add, \n - to subtract, \n * to multiply, \n / to divide \n")

result = None

if math_action == "+" :
    result = num1 + num2
elif math_action == "-" :
    result = num1 - num2
elif math_action == "*" :
    result = num1 * num2
elif math_action == "/" :
    if num2 == 0:
        print("Nope, we dont do that!")
    else:
        result = num1 / num2
else:
    print("You can only choose + - * /")

print(num1, math_action, num2, "=", result)
