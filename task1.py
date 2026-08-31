name = "Nazar"
surname = "Mischuk"
group = "IT-32"
d = 30          
c = 7          

print(f"{name} {surname}, {group}")

count = 0
total_sum = 0
product = 1
even_count = 0
odd_count = 0

print(f"Numbers from {d} to 31:", end=" ")
for number in range(d, 32):        
    print(number, end=" ")
    count += 1
    total_sum += number
    product *= number

    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print()  
average = total_sum / count

print(f"Count: {count}")
print(f"Sum: {total_sum}")
print(f"Product: {product}")
print(f"Average: {average:.2f}")
print(f"Even: {even_count}, odd: {odd_count}")

print("\n# while version")

number = d
count_w = 0
total_sum_w = 0
product_w = 1
even_count_w = 0
odd_count_w = 0

print(f"Numbers from {d} to 31:", end=" ")
while number <= 31:
    print(number, end=" ")
    count_w += 1
    total_sum_w += number
    product_w *= number

    if number % 2 == 0:
        even_count_w += 1
    else:
        odd_count_w += 1

    number += 1  

print()

average_w = total_sum_w / count_w

print(f"Count: {count_w}")
print(f"Sum: {total_sum_w}")
print(f"Product: {product_w}")
print(f"Average: {average_w:.2f}")
print(f"Even: {even_count_w}, odd: {odd_count_w}")

print("Countdown:", end=" ")
for i in range(c, 0, -1):  
    print(i, end=" ")
print()