#soal 1
#======================================================
#bebin 1 nabayad baraye pool float estefade kard chon daghigh nist 2 nabayad dakhele decimal float gozasht chon daqiq nist 3 integer va decimal ok e baraye pool
from decimal import Decimal
0.3 + 0.3 + 0.3 == 0.9 #khata ast
Decimal('0.3') + Decimal('0.3') + Decimal('0.3') == Decimal('0.9') #khata nist
Decimal('0.3') * 3 == Decimal('0.9') #khata nist

#soal 2
#======================================================

#chon dakhlele input hamishe matn tahvil mide che adad vared beshe che chiz dige pas hamishe str ast

type(input("Enter a number: ")) #str ast

#soal 3
#======================================================

10 / 4 #2.5 ast float ast
10 // 4 #2 ast integer ast
2**4 #16 ast integer ast
9%4 #1 ast integer ast baghimande
"4" + "9" #49 ast str ast
Decimal('9') / 4 #2.25 ast decimal ast

#soal 4
#======================================================

name = input("Enter a name: ") #str ast
price = Decimal(input("Enter a price: ")) #decimal ast

print(f'name: {name}, price: {price:,}')