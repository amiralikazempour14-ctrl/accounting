from decimal import Decimal

class Account:
    def __init__(self, code, name, balance=Decimal("0")):
        self.name = name
        self.balance = balance
        self.code = code

    def bedehkar(self, amount):
        self.balance += amount

    def bestankar(self, amount):
        self.balance -= amount

    def gozaresh(self):
        return f"{self.code} -> {self.name}: {self.balance}"

a = Account(1101, "bank")
b = Account(1102, "sandogh")
c = Account(2101, "moshtari")

a.bedehkar(Decimal("100000"))
b.bestankar(Decimal("50000"))
c.bedehkar(Decimal("10000"))
list = [a, b, c]
for account in list:
    print(account.gozaresh())


