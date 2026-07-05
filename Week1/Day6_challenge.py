from decimal import Decimal

totals = {}
counts = {}

while True:
    kind = input("Enter customer type (vije/adi): ").strip().lower()

    if kind == "":
        break

    if kind != "vije" and kind != "adi":
        print("Invalid customer type.")
        continue

    raw = input("Enter amount: ").strip()

    if not raw.isdigit():
        print("Invalid amount.")
        continue

    amount = Decimal(raw)

    if amount <= 0:
        print("Amount must be greater than zero.")
        continue

    if kind in totals:
        totals[kind] += amount
        counts[kind] += 1
    else:
        totals[kind] = amount
        counts[kind] = 1

if len(totals) == 0:
    print("forooshi sabt nashod")
else:
    total_day = Decimal("0")

    for kind, total in totals.items():
        print(f"{kind}:")
        print(f"Count: {counts[kind]}")
        print(f"Total: {total:,}")

        total_day += total

    print(f"Total day: {total_day:,}")