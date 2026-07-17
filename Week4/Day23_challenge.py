import json
from decimal import Decimal

daftar = {
    "accounts": [
        {"code": "1101", "name": "صندوق"},
        {"code": "4101", "name": "فروش"}
    ],
    "vouchers": [
        {
            "shomare": 1,
            "sharh": "فروش نقدی",
            "lines": [
                {"code": "1101", "bedehkar": "5000000", "bestankar": "0"},
                {"code": "4101", "bedehkar": "0", "bestankar": "5000000"}
            ]
        },
        {
            "shomare": 2,
            "sharh": "پرداخت هزینه",
            "lines": [
                {"code": "6101", "bedehkar": "1000000", "bestankar": "0"},
                {"code": "1101", "bedehkar": "0", "bestankar": "1000000"}
            ]
        }
    ]
}

with open("daftar.json", "w", encoding="utf-8") as file:
    json.dump(daftar, file, ensure_ascii=False, indent=2)

try:
    with open("daftar.json", "r", encoding="utf-8") as file:
        daftar = json.load(file)

    # جمع کل همه اسناد
    grand_total_bedehkar = Decimal("0")
    grand_total_bestankar = Decimal("0")

    for voucher in daftar["vouchers"]:

        # جمع هر سند
        total_bedehkar = Decimal("0")
        total_bestankar = Decimal("0")

        for line in voucher["lines"]:
            bedehkar = Decimal(line["bedehkar"])
            bestankar = Decimal(line["bestankar"])

            total_bedehkar += bedehkar
            total_bestankar += bestankar

            grand_total_bedehkar += bedehkar
            grand_total_bestankar += bestankar

        if total_bedehkar == total_bestankar:
            print(f"Voucher {voucher['shomare']} -> Balanced")
        else:
            print(f"Voucher {voucher['shomare']} -> Not Balanced")

    print()

    if grand_total_bedehkar == grand_total_bestankar:
        print("Golden Test: PASSED")
    else:
        print("Golden Test: FAILED")
        print(f"Difference: {grand_total_bedehkar - grand_total_bestankar}")

except FileNotFoundError:
    print("فایل daftar.json یافت نشد")

except json.JSONDecodeError:
    print("فایل daftar.json معتبر نیست")