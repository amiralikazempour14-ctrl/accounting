from decimal import Decimal

shomare_sanad = 0
largest = 0
total = 0

while True:
    raw = input("Enter a number or press Enter to quit: ")
    if raw == "":
        break
    else:
        number = Decimal(raw)
        if number > 0:
            shomare_sanad += 1
            total += number
            if number > largest:
                largest = number
        else:
            print("Number is negative or zero")
            continue
if shomare_sanad > 0:
    miangin = total / shomare_sanad
    print(f"Total numbers entered: {shomare_sanad:,}")
    print(f"Total sum: {total:,}")
    print(f"Average: {miangin.quantize(Decimal('1')):,}")
    print(f"Largest number: {largest:,}")
else:
    print("No data")