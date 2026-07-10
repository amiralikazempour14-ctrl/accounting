from decimal import Decimal


class Account:
    def __init__(self, code, name, balance="0"):
        self.code = code
        self.name = name
        self._balance = Decimal(balance)

    def bedehkar(self, amount):
        amount = Decimal(amount)

        if amount <= Decimal("0"):
            raise ValueError("Amount must be positive")

        self._balance += amount

    def bestankar(self, amount):
        amount = Decimal(amount)

        if amount <= Decimal("0"):
            raise ValueError("Amount must be positive")

        self._balance -= amount

    def __repr__(self):
        return f"[{self.code}] {self.name}-> {self._balance}"

    def __eq__(self, other):
        if not isinstance(other, Account):
            return NotImplemented
        return self.code == other.code

    def __lt__(self, other):
        if not isinstance(other, Account):
            return NotImplemented
        return self.code < other.code

a = Account("1103", "bank3")
b = Account("1101", "bank1")
c = Account("2101", "customer")
d = Account("1102", "cash")
e = Account("5101", "capital")

a.bedehkar(100000)
b.bedehkar(200000)
c.bedehkar(300000)
d.bedehkar(400000)
e.bedehkar(500000)

accounts = [a, b, c, d, e]
print(sorted(accounts))

f = Account("1103", "bank8")
print(a == f)
