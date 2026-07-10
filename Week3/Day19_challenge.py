from decimal import Decimal


class VoucherLine:
    def __init__(
        self,
        voucher_code,
        debit_amount="0",
        credit_amount="0"
    ):
        self.voucher_code = voucher_code
        self.debit_amount = Decimal(debit_amount)
        self.credit_amount = Decimal(credit_amount)

        if self.debit_amount < Decimal("0"):
            raise ValueError("Debit amount cannot be negative")

        if self.credit_amount < Decimal("0"):
            raise ValueError("Credit amount cannot be negative")

        if (
            self.debit_amount > Decimal("0")
            and self.credit_amount > Decimal("0")
        ):
            raise ValueError(
                "A voucher line cannot be both debit and credit"
            )

    def __repr__(self):
        return (
            f"{self.voucher_code}: "
            f"debit={self.debit_amount:,} "
            f"credit={self.credit_amount:,}"
        )


class Voucher:
    def __init__(self, code):
        self.code = code
        self.lines = []
        self.sabt_shode = False

    def add_line(self, line):
        self.lines.append(line)

    def total_debit(self):
        return sum(
            (line.debit_amount for line in self.lines),
            Decimal("0")
        )

    def total_credit(self):
        return sum(
            (line.credit_amount for line in self.lines),
            Decimal("0")
        )

    def taraze(self):
        return self.total_debit() == self.total_credit()

    def sabt(self):
        if len(self.lines) < 2:
            raise ValueError(
                "Voucher must have at least two lines"
            )

        if self.total_debit() == Decimal("0"):
            raise ValueError(
                "Voucher total cannot be zero"
            )

        if not self.taraze():
            raise ValueError(
                f"Voucher is not balanced: "
                f"debit={self.total_debit()} "
                f"credit={self.total_credit()}"
            )

        self.sabt_shode = True


# Scenario 1: valid and balanced voucher

v1 = Voucher(1)

v1.add_line(
    VoucherLine(
        "1101",
        debit_amount="1000"
    )
)

v1.add_line(
    VoucherLine(
        "2101",
        credit_amount="1000"
    )
)

v1.sabt()

print(v1.lines)
print(v1.total_debit())
print(v1.total_credit())
print(v1.sabt_shode)


# Scenario 2: unbalanced voucher

try:
    v2 = Voucher(2)

    v2.add_line(
        VoucherLine(
            "1101",
            debit_amount="1000"
        )
    )

    v2.add_line(
        VoucherLine(
            "2101",
            credit_amount="600"
        )
    )

    v2.sabt()

except ValueError as e:
    print(e)


# Scenario 3: one line is both debit and credit

try:
    invalid_line = VoucherLine(
        "1101",
        debit_amount="100",
        credit_amount="50"
    )

except ValueError as e:
    print(e)