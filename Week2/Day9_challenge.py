from decimal import Decimal

khaam = [
    " 500000 ",
    "abc",
    "1200000",
    "",
    "-300000",
    " 2500000",
    "0",
    "750000 "
]

# Stage 1: Clean
tamiz = [x.strip() for x in khaam if x.strip() != ""]

# Stage 2: Numeric
adadi = [Decimal(x) for x in tamiz if x.isdigit()]

# Stage 3: Valid sales
motabar = [x for x in adadi if x > 0]

# Stage 4: Report
if len(motabar) == 0:
    print("forooshi sabt nashod")
    exit()

print(f"Total raw data: {len(khaam)}")
print(f"Total valid sales: {len(motabar)}")
print(f"Total removed: {len(khaam) - len(motabar)}")
print(f"Total sales: {sum(motabar):,}")
print(f"Largest sale: {max(motabar):,}")
