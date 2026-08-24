day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if year <= 0:
    print("Date is invalid: year is not positive")

elif month < 1 or month > 12:
    print("Date is invalid: wrong month")

elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        if day >= 1 and day <= 29:
            print("Date is valid")
        else:
            print("Date is invalid: wrong day")
    else:
        if day >= 1 and day <= 28:
            print("Date is valid")
        else:
            print("Date is invalid: wrong day")

elif month == 4 or month == 6 or month == 9 or month == 11:
    if day >= 1 and day <= 30:
        print("Date is valid")
    else:
        print("Date is invalid: wrong day")

else:
    if day >= 1 and day <= 31:
        print("Date is valid")
    else:
        print("Date is invalid: wrong day")