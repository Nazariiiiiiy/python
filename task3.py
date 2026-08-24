a = float(input("Введіть перше число "))
operation = input("Виберіть операцію ")
b = float(input("Введіть друге число "))

if operation == "+":
    result = a + b 
    print(f"{a}+{b} = {result:.4f}")
elif operation == "-":
    result = a - b
    print(f"{a}-{b} = {result:.4f}")
elif operation == "*":
    result = a * b
    print(f"{a}*{b} = {result:.4f}")
elif operation == "/":
    if b == 0:
        print("На нуль ділити не можна!")
    else:
        result = a / b
        print(f"{a} / {b} = {result:.4f}")
elif operation == "//":
    if b == 0:
        print("На нуль ділити не можна!")
    else:
        result = a // b
        print(f"{a} // {b} = {result:.4f}")
elif operation == "%":
    if b == 0:
        print("На нуль ділити не можна!")
    else:
        result = a % b
        print(f"{a} % {b} = {result:.4f}")
elif operation == "**":
    result = a ** b
    print(f"{a} ** {b} = {result:.4f}")
else:
    print("Невідома операція")