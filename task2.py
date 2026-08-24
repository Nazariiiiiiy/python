number = int(input("Введіть ціле число"))

if number > 0: 
    print("Число додатнє")
elif number < 0:
    print(" Число негативне")
else:
    print("ЧИсло є 0")
if number != 0:
    if number % 2 == 0:
        print("Число парне")
    else:
        print("Число не парне")
    