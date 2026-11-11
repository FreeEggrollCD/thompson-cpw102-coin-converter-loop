# CPW 101 Programming Assignment 7
# This file contains starter code for the following:

# Modify a previous program so that the user
# can use its code as many times as they wish.

CENTS_PER_QUARTER = 25 # a quarter is 25 cents
CENTS_PER_DIME = 10    # a dime is 10 cents
CENTS_PER_NICKEL = 5   # a nickel is 5 cents

# The original program calculated the value of some coins.
converting:bool = True
is_negative:bool = False
sum_nums:list = []

while converting:
    print('We will convert coins to cents.')
    quarters = int(input('How many quarters? '))
    dimes = int(input('How many dimes? '))
    nickels = int(input('How many nickels? '))
    pennies = int(input('How many pennies? '))

    cents = CENTS_PER_QUARTER * quarters \
          + CENTS_PER_DIME * dimes \
          + CENTS_PER_NICKEL * nickels \
          + pennies

    print( quarters, 'quarters',
           dimes, 'dimes',
           nickels, 'nickels',
           pennies, 'pennies',
           'is', cents, 'cents.')

    if input('Convert more coins? (y/n) ').lower().strip() != 'y':
        converting = False

while not is_negative:
    num = int(input('Enter a number: '))
    if num < 0:
        is_negative = True
    else:
        sum_nums.append(num)
print(sum(sum_nums))
