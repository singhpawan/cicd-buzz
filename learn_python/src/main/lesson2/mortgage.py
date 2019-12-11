#!/usr/bin/env python3

# mortgage.py
#
# Find out how to payoff a mortgage

principal = 500000
payment = 2684.11
rate = 0.05
total_paid = 0

# Extra payment Info
extra_payment = 1000
extra_payment_start_month = 1
extra_payment_end_month = 60
month = 0

out = open('schedule.txt', 'w') # open a file for writing
print('{:>5s} {:>10s} {:>10s} {:>10s}'.format('month', 'interest', 'remaining', 'principal'),file=out)
while principal > 0:
    month += 1
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        total_payment = payment + extra_payment
    else:
        total_payment = payment
    interest = principal*(rate/12)
    principal = principal + interest - total_payment
    total_paid += total_payment
    print('{:>5d} {:>10.2f} {:>10.2f} {:>10.2f}'.format(month, interest, total_payment - interest, principal),file=out)

out.close()
print("Total Paid: ", total_paid)


'''
name = 'IBM'
shares = 2000
price = 23.20
print('%10s %10d %10.2f' %(name, price, shares))
print('{:>10s} {:>10d} {:>10.2f}'.format(name, shares, price)) //right justify
print('{:<10s} {:<10d} {:<10.2f}'.format(name, shares, price)) //left justify
'''

