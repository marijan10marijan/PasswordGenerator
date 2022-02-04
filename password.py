## Password generator in Python
import random

numbers = '0123456789'
lower_letters = 'abcdefghijklmnopqrstuvwxyz'
upper_letters = lower_letters.upper()
symbols = '()[]{}*?#$&/"!-.;:<>'

together = numbers + lower_letters + upper_letters + symbols

## Single password
length = 20
password = ''.join(random.sample(together,length))
print(password)

## Set amount of passwords
length = 25
amount = 10

for i in range(amount):
    password = ''.join(random.sample(together,length))
    print(password)

## If don't want some parametar...We can set symbols as False or numbers as False

all = ''
nums, lower, upper, symb = True, True, True, False
if nums:
    all += numbers
if lower:
    all += lower_letters
if upper:
    all += upper_letters
if symb:
    all += symbols

password = ''.join(random.sample(all,20))
print(password)




