from decimal import Decimal

sanad = [
    ("1101", "5000000", "0"),
    ("4101", "0", "5000000")
]

with open("sanad.txt", "w", encoding="utf-8") as file:
    for code, bedehkar, bestankar in sanad:
        file.write(f"{code},{bedehkar},{bestankar}\n")

total_debit = Decimal("0")
total_credit = Decimal("0")

try:
    with open("sanad.txt", "r", encoding="utf-8") as file:
        for line in file:
            code, bedehkar, bestankar = line.strip().split(",")

            debit = Decimal(bedehkar)
            credit = Decimal(bestankar)

            total_debit += debit
            total_credit += credit

    if total_debit == total_credit:
        print("Sanad taraz ast.")
    else:
        print("Sanad taraz nist.")
        difference = abs(total_debit - total_credit)
        print(f"Ekhtelaf: {difference}")

except FileNotFoundError:
    print("File sanad.txt peyda nashod.")