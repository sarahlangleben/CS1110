"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and
an amount. It prints out the result of converting the first currency to
the second.

Author: Sarah Langleben, sml343, Nicole Yatskar (ny73)
Date: 9/30/2020
"""
import a1

old = input('Enter source currency: ')
new = input('Enter target currency: ')
amt = float(input('Enter original amount: '))

final = a1.exchange(old,new,amt)

print('You can exchange ' + str(amt) + ' ' +  old  + ' for ' + str(final) + ' ' + new + '.')
