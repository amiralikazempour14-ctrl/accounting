from decimal import Decimal

#sec1
########################################################

print(17//5, 17%5) #3, 2
print(2%7) #2
print(2 + 3 * 4) #14
print((2 + 3) * 4) #20
print(2 ** 3 ** 2) #512
print(10 % 2 == 0) #True bool

#sec2
########################################################

print(True and False) #False bool
print(True or False) #True bool
print(not True and False) #False bool
print(not(True and False)) #True bool
print(7 % 2 == 1 and not False) #True bool
print(5 > 3 or 10 / 1 > 1) #True bool chon yekish dorost bashe kafie

#tamrin 1
########################################################

mablagh = 100000000
travel_100k_rial = mablagh // 1000000
baghimande = mablagh % travel_100k_rial
print(travel_100k_rial, baghimande) #10, 0

travel_50k_rial = baghimande // 500000
baghimande = mablagh - travel_50k_rial * 500000
print(travel_50k_rial, baghimande) #1, 0

travel_10k_rial = baghimande // 10000
baghimande = mablagh - travel_10k_rial * 10000
print(travel_10k_rial, baghimande) #100, 0
