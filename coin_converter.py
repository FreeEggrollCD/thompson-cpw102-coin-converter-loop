# CPW 101 Programming Assignment 7
# This file contains starter code for the following:

# Modify a previous program so that the user
# can use its code as many times as they wish.

CENTS_PER_QUARTER = 25 # a quarter is 25 cents
CENTS_PER_DIME = 10    # a dime is 10 cents
CENTS_PER_NICKEL = 5   # a nickel is 5 cents

# The original program calculated the value of some coins.

# get input
print('We will convert coins to cents.')
quarters = int(input('How many quarters? '))
dimes = int(input('How many dimes? '))
nickels = int(input('How many nickels? '))
pennies = int(input('How many pennies? '))

# process the input,
# calculate the total value, in cents,
# of the coins input by the user.
cents = CENTS_PER_QUARTER * quarters \
      + CENTS_PER_DIME * dimes \
      + CENTS_PER_NICKEL * nickels \
      + pennies

# display the original coin quantities
# and the calculated value.
print( quarters, 'quarters',
       dimes, 'dimes',
       nickels, 'nickels',
       pennies, 'pennies',
       'is', cents, 'cents.')

