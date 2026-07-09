from decimal import Decimal


class Account:
    counter = 0

    def __init__(self, code, name, balance="0"):
        Account.counter += 1

        self.id = Account.counter
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

    def gozaresh(self):
        return f"#{self.id} [{self.code}] {self.name} -> mande: {self._balance}"


a = Account("1101", "bank")
b = Account("1102", "sandogh")
c = Account("2101", "moshtari")

a.bedehkar("1000.50")
a.bestankar("200.25")

b.bedehkar("500.75")

c.bedehkar("300.00")
c.bestankar("50.25")

accounts = [a, b, c]

for account in accounts:
    print(account.gozaresh())

try:
    c.bestankar("-5")
except ValueError as e:
    print(e)