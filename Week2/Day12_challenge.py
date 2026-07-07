from decimal import Decimal, InvalidOperation

sales = []
def get_price(prompt):
    while True:
        x = input(prompt).strip()
        try:
            if x == "":
                return None
            price = Decimal(x)
            if price <= Decimal("0"):
                print("Price must be positive and non-zero")
                continue
            return price
        except InvalidOperation:
            print("Invalid input")
            continue

while True:
    price = get_price("Enter price: ")
    if price is None:
        break
    sales.append(price)

if len(sales) == 0:
    print("No sales")
else:
    print("number of Sales:", len(sales))

    total = Decimal("0")
    for i in sales:
        total += i
    print(f"Total sales: {total}")

    average = total / len(sales)
    print(f"Average sales: {average}")

    max_sale = Decimal("0")
    for i in sales:
        if i > max_sale:
            max_sale = i
    print(f"Max sales: {max_sale}")
    