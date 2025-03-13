import math


def is_year_leap(year):
    return year % 4 == 0


def square(side):
    return math.ceil(side ** 2)


year = 2024
result = is_year_leap(year)
print(f'год {year}: {result}')
