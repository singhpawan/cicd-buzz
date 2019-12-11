#!/usr/bin/env python3

import csv
import sys

def read_portfolio(filename, *, errors="warn"):
    '''
    Read a csv file with name, shares, price data into a list,
    '''

    if errors not in {'warn', 'raise', 'silent'}:
        raise ValueError("errors must be one of 'warn', 'raise', 'silent' ")
    portfolio = [] # list of records

    total = 0.0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        header = next(f)
        for rowno, row in enumerate(rows, start=1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:
                if errors == "warn":
                    print("Row", rowno, "Bad Row:", row)
                    print("Reason", err)
                elif errors == "raise":
                    raise # reraises the last exception
                else:
                    pass
                continue
            #record = tuple(row)
            record = {
                'name': row[0],
                'date': row[1],
                'shares': row[2],
                'price': row[3]

            }
            portfolio.append(record)
            total += row[2] * row[3]
    return portfolio


#print("Total Cost: ", read_portfolio('missing.csv',errors='silent'))

portfolio = read_portfolio('./portfolio.csv')
print(portfolio)

'''
total = 0.0
for holding in portfolio:
    total += holding[2] * holding[3] # this is not readable

print(total)

better_total =0.0
for name, date, shares, price in portfolio:
    better_total += shares * price

print("Better Total", better_total)
'''

# this is good for building list of dictionaries
dictionary_total = 0.0
for holding in portfolio:
    dictionary_total += holding['shares'] * holding['price']

print(dictionary_total)

# so now if we have a large number of variables it hard to print out all of them.
# there's a better idea to modify the tuple in read_portfolio and make the record a dictionary

# python -i port.py



# list of dictionaries is that it works well with json encoding and other data formats.

# import json
#data = json.dumps(poryfolio)

# Then ship this data across the network.

# data = json.load(portfolio)

# it is a good starting points and take contents of a file and then start working with it.



# 5.3

