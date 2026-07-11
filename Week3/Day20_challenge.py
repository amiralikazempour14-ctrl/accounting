from dataclasses import dataclass
from decimal import Decimal


@dataclass
class VoucherLine:
    hesab_code: str
    bedehkar: str = "0"
    bestankar: str = "0"

    def __post_init__(self):
        self.bedehkar = Decimal(self.bedehkar)
        self.bestankar = Decimal(self.bestankar)

        if self.bedehkar < Decimal("0") or self.bestankar < Decimal("0"):
            raise ValueError("Amounts cannot be negative")

        if (
            self.bedehkar > Decimal("0")
            and self.bestankar > Decimal("0")
        ):
            raise ValueError(
                "A voucher line cannot be both debit and credit"
            )


class Voucher:
    def __init__(self, shomare):
        self.shomare = shomare
        self.lines = []
        self.sabt_shode = False

    def add_line(self, line):
        self.lines.append(line)

    @property
    def jam_bedehkar(self):
        return sum(
            (line.bedehkar for line in self.lines),
            Decimal("0")
        )

    @property
    def jam_bestankar(self):
        return sum(
            (line.bestankar for line in self.lines),
            Decimal("0")
        )

    @property
    def taraz_ast(self):
        return self.jam_bedehkar == self.jam_bestankar

    @property
    def tedad_khotoot(self):
        return len(self.lines)

    def sabt(self):
        if self.tedad_khotoot < 2:
            raise ValueError(
                "Voucher must have at least two lines"
            )

        if self.jam_bedehkar == Decimal("0"):
            raise ValueError(
                "Voucher total cannot be zero"
            )

        if not self.taraz_ast:
            raise ValueError(
                f"Voucher is not balanced: "
                f"debit={self.jam_bedehkar} "
                f"credit={self.jam_bestankar}"
            )

        self.sabt_shode = True


# Scenario 1: valid and balanced voucher

v = Voucher(1)

v.add_line(
    VoucherLine(
        "1101",
        bedehkar="1000"
    )
)

v.add_line(
    VoucherLine(
        "2101",
        bestankar="1000"
    )
)

print(v.tedad_khotoot)
print(v.jam_bedehkar)
print(v.jam_bestankar)
print(v.taraz_ast)
print(v.lines)

v.sabt()

print(v.sabt_shode)


# Scenario 2: unbalanced voucher

try:
    bad = Voucher(2)

    bad.add_line(
        VoucherLine(
            "1101",
            bedehkar="1000"
        )
    )

    bad.add_line(
        VoucherLine(
            "2101",
            bestankar="600"
        )
    )

    bad.sabt()

except ValueError as e:
    print(e)


# Scenario 3: one line is both debit and credit

try:
    VoucherLine(
        "1101",
        bedehkar="100",
        bestankar="50"
    )

except ValueError as e:
    print(e)