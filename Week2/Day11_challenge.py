from decimal import Decimal


def get_item():
    name = input("Enter item name: ").strip()

    if name == "":
        return None

    price = input("Enter item price: ")

    if not price.isdigit() or Decimal(price) <= Decimal("0"):
        print("Price must be a positive number.")
        return None

    quantity = input("Enter quantity: ")

    if not quantity.isdigit() or int(quantity) <= 0:
        print("Quantity must be a positive number.")
        return None

    return {
        "name": name,
        "price": Decimal(price),
        "quantity": int(quantity)
    }


def item_total(item):
    return item["price"] * item["quantity"]


def cart_report(cart):
    if len(cart) == 0:
        return 0, Decimal("0"), None

    count = len(cart)

    total = Decimal("0")
    max_value = Decimal("0")
    max_item = None

    for item in cart:
        value = item_total(item)
        total += value

        if value > max_value:
            max_value = value
            max_item = item

    return count, total, max_item


# ---------------- Main ----------------

cart = []

while True:
    item = get_item()

    if item is None:
        break

    cart.append(item)

count, total, max_item = cart_report(cart)

if count == 0:
    print("No data")
else:
    print("\nCart Items")
    print("-" * 40)

    for index, item in enumerate(cart, start=1):
        print(f"Item {index}")
        print(f"Name: {item['name']}")
        print(f"Price: {item['price']}")
        print(f"Quantity: {item['quantity']}")
        print(f"Total: {item_total(item)}")
        print("-" * 40)

    print(f"Total items: {count}")
    print(f"Grand total: {total}")
    print("Most expensive item:")
    print(f"Name: {max_item['name']}")
    print(f"Price: {max_item['price']}")
    print(f"Quantity: {max_item['quantity']}")
    print(f"Total: {item_total(max_item)}")