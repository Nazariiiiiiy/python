name = "Nazar"
surname = "Mischuk"
group = "IT-32"

print(f"{name} {surname}, {group}")

number = int(input("Enter an integer: "))

if number <= 0:
    print("Number must be positive")
else:
    digits_count = 0
    digits_sum = 0
    max_digit = 0
    min_digit = 9
    reversed_number = 0

    temp = number
    while temp > 0:
        last_digit = temp % 10      

        digits_count += 1
        digits_sum += last_digit

        if last_digit > max_digit:
            max_digit = last_digit
        if last_digit < min_digit:
            min_digit = last_digit

        reversed_number = reversed_number * 10 + last_digit
        temp = temp // 10           

    print(f"Digits: {digits_count}")
    print(f"Sum of digits: {digits_sum}")
    print(f"Max digit: {max_digit}, min digit: {min_digit}")
    print(f"Reversed: {reversed_number}")