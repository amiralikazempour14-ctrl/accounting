from decimal import Decimal

faktor = []

while True:
    raw = input("Enter amount (Enter to quit): ").strip()

    if raw == "":
        break

    try:
        mablagh = Decimal(raw)
    except:
        print("Invalid amount.")
        continue

    if mablagh <= 0:
        print("Amount must be greater than zero.")
        continue

    faktor.append(mablagh)

if len(faktor) == 0:
    print("faktor khali ast")
else:
    print("Aghlam:")

    for i, amount in enumerate(faktor, start=1):
        print(f"{i}. {amount:,}")

    jam = sum(faktor)
    tedad = len(faktor)
    miangin = jam / tedad
    geran = max(faktor)
    arzan = min(faktor)

    print(f"Count   : {tedad}")
    print(f"Sum     : {jam:,}")
    print(f"Average : {miangin:,}")
    print(f"Max     : {geran:,}")
    print(f"Min     : {arzan:,}")