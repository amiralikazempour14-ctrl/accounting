from decimal import Decimal

mablagh = Decimal(input("mablagh ra vared konid: "))
if mablagh <= 0:
    print("mablagh not valid")
    exit()

class_moshtari = int(input("class moshtari (1: adi, 2: vije): "))

if class_moshtari == 2:
    print("moshtari vije ast")
    if mablagh >= 5000000:
        takhfif = mablagh * Decimal("0.10")
    else:
        takhfif = mablagh * Decimal("0.05")
elif class_moshtari == 1:
    print("moshtari adi ast")
    if mablagh >= 10000000:
        takhfif = mablagh * Decimal("0.02")
    else:
        takhfif = Decimal("0")
else:
    print("class moshtari not valid")
    exit()

mablagh_nahaei = mablagh - takhfif
print(f"mablagh avvalie: {mablagh:,}")
print(f"takhfif: {takhfif:,}")
print(f"mablagh nahaei: {mablagh_nahaei:,}")

# shekastan be esknas — cascade: rooye baghimande edame bede
noteh_1m = mablagh_nahaei // 1000000
baghi = mablagh_nahaei % 1000000
noteh_100k = baghi // 100000
baghi = baghi % 100000
print(f"esknas 1,000,000: {noteh_1m} adad")
print(f"esknas 100,000:   {noteh_100k} adad")
print(f"baghimande:       {baghi:,}")