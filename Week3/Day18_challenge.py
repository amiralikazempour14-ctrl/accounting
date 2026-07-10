from decimal import Decimal

class Account:
    def __init__(self, code, name, balance="0"):
        self._code = code
        self._name = name
        self._balance = Decimal(balance)

    def debit(self, amount):
        amount = Decimal(amount)
        
        if amount <= Decimal("0"):
            raise ValueError("Amount must be greater than 0")

        self._balance += amount

    def credit(self, amount):
        amount = Decimal(amount)
        
        if amount <= Decimal("0"):
            raise ValueError("Amount must be greater than 0")

        self._balance -= amount

    def report(self):
        return f"[{self._code}] {self._name} -> {self._balance}"

class SavingsAccount(Account):
    def __init__(self, code, name, balance="0", interest_rate="0"):
        super().__init__(code, name, balance)
        self._interest_rate = Decimal(interest_rate)

    def interest(self):
        return self._balance * self._interest_rate

    def report(self):
        return f"{super().report()} | intrest={self.interest()}"

a = Account("1101", "Bank")
b = SavingsAccount("1102", "savings", interest_rate="0.20")
a.debit("100000")
a.credit("50000")
b.debit("100000")
b.credit("50000")

print(a.report())
print(b.report())
print(b.interest())

print(isinstance(b, SavingsAccount))
print(isinstance(b, Account))
print(isinstance(a, SavingsAccount))

