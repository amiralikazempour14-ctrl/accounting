from decimal import Decimal
from dataclasses import dataclass

@dataclass
class VoucherLine:
    code: str
    bedehkar: str
    bestankar: str

    def __post_init__(self):
        self.bedehkar = Decimal(self.bedehkar)
        self.bestankar = Decimal(self.bestankar)

        if self.bedehkar < Decimal("0") or self.bestankar < Decimal("0"):
            raise ValueError("Amounts cannot be negative")

        if (
            self.bedehkar > Decimal("0")
            and self.bestankar > Decimal("0")
        ):
            raise ValueError("A voucher line cannot be both debit and credit")

class Account:
    def __init__(self, code, name, type):
        self.code = code
        self.name = name
        self.type = type

    def __repr__(self):
        return f"[{self.code}] {self.name}: ({self.type})"

class Voucher:
    shomare = 0
    def __init__(self, sharh):
        Voucher.shomare += 1
        self.shomare = Voucher.shomare
        self.lines = []
        self.sharh = sharh
        self.sabt_shode = False

    def add_line(self, line):
        self.lines.append(line)


    @property
    def total_bedehkar(self):
        return sum((line.bedehkar for line in self.lines), Decimal("0"))

    @property
    def total_bestankar(self):
        return sum((line.bestankar for line in self.lines), Decimal("0"))

    @property
    def taraz(self):
        return self.total_bedehkar == self.total_bestankar

    @property
    def tedad_khotoot(self):
        return len(self.lines)


    def sabt(self):
        if self.tedad_khotoot < 2:
            raise ValueError("Voucher must have at least two lines")

        if self.total_bedehkar == Decimal("0"):
            raise ValueError("Voucher total cannot be zero")

        if not self.taraz:
            raise ValueError("Voucher is not balanced")

        self.sabt_shode = True

class Daftar:
    def __init__(self):
        self.vouchers = []
        self.accounts = []

def add_voucher(self, voucher):
    voucher.sabt()
    self.vouchers.append(voucher)

    def mande(self, code):
        total_bedehkar = Decimal("0")
        total_bestankar = Decimal("0")
        for voucher in self.vouchers:
            for line in voucher.lines:
                if line.code == code:
                    total_bedehkar += line.bedehkar
                    total_bestankar += line.bestankar
        return total_bedehkar - total_bestankar

    def add_account(self, account):
        self.accounts.append(account)

    def taraz_azmayeshi(self):
        report = []
        for account in self.accounts:
            report.append(
                (account.code, account.name, self.mande(account.code))
            )
        return report

@dataclass
class Kala:
    code: str
    name: str
    price: str = "0"
    mojoodi: int = 0

    def __post_init__(self):
        self.price = Decimal(self.price)

        if self.price < Decimal("0"):
            raise ValueError("Price cannot be negative")

        if not isinstance(self.mojoodi, int):
            raise ValueError("Quantity must be an integer")

        if self.mojoodi < 0:
            raise ValueError("Quantity cannot be negative")

class Anbar:
    def __init__(self):
        self.kala = []

    def add_kala(self, kala):
        for existing_kala in self.kala:
            if existing_kala.code == kala.code:
                raise ValueError("Kala already exists")

        self.kala.append(kala)

    def vorood(self, code, tedad):
        if not isinstance(tedad, int):
            raise ValueError("Quantity must be an integer")

        if tedad <= 0:
            raise ValueError("Quantity must be greater than zero")

        for kala in self.kala:
            if kala.code == code:
                kala.mojoodi += tedad
                return

        raise ValueError("Kala not found")

    def khrooj(self, code, tedad):
        if not isinstance(tedad, int):
            raise ValueError("Quantity must be an integer")

        if tedad <= 0:
            raise ValueError("Quantity must be greater than zero")

        for kala in self.kala:
            if kala.code == code:
                if kala.mojoodi < tedad:
                    raise ValueError(
                        f"Not enough inventory: requested {tedad}, available {kala.mojoodi}"
                    )

                kala.mojoodi -= tedad
                return

        raise ValueError("Kala not found")