from decimal import Decimal

name = input("Enter a name: ") #str ast
price_per_month = Decimal(input("Enter a price: ")) #decimal ast
months = int(input("Enter the number of monthes: ")) #int ast

total_price = price_per_month * months
insurance_price = total_price * Decimal('0.07')
print(f'name: {name}')
print(f'monthly price: {price_per_month:,}')
print(f'total price: {total_price:,}')
print(f'insurance price: {insurance_price:,}')
#bime zarar mikard
