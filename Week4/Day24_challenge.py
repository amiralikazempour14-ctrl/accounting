import csv
from decimal import Decimal

accounts = []

total_balance = Decimal("0")

with open("accounts.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        accounts.append(row)

        if row["balance"] == "":
            print(f'Balance khali ast: {row["code"]}')
            continue

        total_balance += Decimal(row["balance"])

print(f"Total balance: {total_balance:,}")
print(f"Total accounts: {len(accounts)}")