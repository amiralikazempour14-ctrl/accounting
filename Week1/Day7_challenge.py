from decimal import Decimal

sell_list = []

while True:
    customer_data = {}

    name = input("Enter the name: ").strip().lower()
    if name == "":
        break

    raw = input("Enter the price: ")
    if not raw.isdigit():
        print("Price must be a number!")
        continue

    price = Decimal(raw)
    if price <= 0:
        print("Price must be above zero.")
        continue

    raw2 = input("Enter the quantity: ")
    if not raw2.isdigit():
        print("Quantity must be a number!")
        continue

    quantity = int(raw2)
    if quantity <= 0:
        print("Quantity must be above zero.")
        continue

    factor_value = price * quantity

    customer_data["name"] = name
    customer_data["price"] = price
    customer_data["quantity"] = quantity
    customer_data["factor_value"] = factor_value

    sell_list.append(customer_data)

if len(sell_list) == 0:
    print("No data.")
    exit()

print("\n===== FACTOR =====")

for shomare, item in enumerate(sell_list, start=1):
    print(f"{shomare}:")
    for key, value in item.items():
        print(f"{key}: {value:,}" if isinstance(value, Decimal) else f"{key}: {value}")
    print("-" * 30)

max_value = Decimal("0")
max_item = None

for item in sell_list:
    if item["factor_value"] > max_value:
        max_value = item["factor_value"]
        max_item = item

print(f"Most expensive item: {max_item['name']} ({max_value:,})")

print(f"Number of items: {len(sell_list)}")

total_value = Decimal("0")
for item in sell_list:
    total_value += item["factor_value"]

print(f"Total value: {total_value:,}")