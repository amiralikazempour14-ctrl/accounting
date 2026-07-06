from decimal import Decimal


def discount(price, kind):
    if kind == "vije":
        if price >= Decimal("5000000"):
            discount_value = price * Decimal("0.10")
        else:
            discount_value = price * Decimal("0.05")

    elif kind == "adi":
        if price >= Decimal("10000000"):
            discount_value = price * Decimal("0.02")
        else:
            discount_value = Decimal("0")

    else:
        return None, None

    final_price = price - discount_value
    return discount_value, final_price


def counter(price):
    bill_1000000 = price // 1000000

    remain = price % 1000000

    bill_100000 = remain // 100000

    remain = remain % 100000

    return bill_1000000, bill_100000, remain


def valid_code(code):
    code = code.strip()

    return len(code) == 8 and code.isdigit()


def sales_report(sales):
    if len(sales) == 0:
        return 0, Decimal("0"), None

    total = Decimal("0")

    for sale in sales:
        total += sale

    max_value = sales[0]

    for sale in sales:
        if sale > max_value:
            max_value = sale

    return len(sales), total, max_value


# -----------------------
# Tests
# -----------------------

d, f = discount(Decimal("6000000"), "vije")
print(f"Discount: {d:,} | Final: {f:,}")

d, f = discount(Decimal("12000000"), "adi")
print(f"Discount: {d:,} | Final: {f:,}")

d, f = discount(Decimal("5000000"), "test")
print(d, f)

b1, b2, r = counter(3650000)
print(f"1M: {b1} | 100K: {b2} | Remain: {r:,}")

b1, b2, r = counter(850000)
print(f"1M: {b1} | 100K: {b2} | Remain: {r:,}")

print(valid_code("10203040"))
print(valid_code("1020a040"))

count, total, maximum = sales_report([
    Decimal("500000"),
    Decimal("1200000"),
    Decimal("750000")
])

print(f"Count: {count}")
print(f"Total: {total:,}")
print(f"Maximum: {maximum:,}")

count, total, maximum = sales_report([])
print(count, total, maximum)
