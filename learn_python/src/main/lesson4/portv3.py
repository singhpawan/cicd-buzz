#!/usr/bin/env python3

import csv
import sys

def portfolio_cost(filename, *, errors="warn"):
    '''
    Computes total shares*price for a csv file with name,date,shares,price data
    :param filename:
    :return: the total value of the portfolio
    '''
    # telling the users that the errors have to be one of these inputs.
    # and it catches unexpected input from the user and it will and being defenseive is good.
    if errors not in {'warn', 'raise', 'silent'}:
        raise ValueError("errors must be one of 'warn', 'raise', 'silent' ")

    total = 0.0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        header = next(f)
        for rowno, row in enumerate(rows, start=1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:
            #except Exception as err: # Catches all errors ( diaper pattern) catches everything
                if errors == "warn":
                    print("Row", rowno, "Bad Row:", row)
                    print("Reason", err)
                elif errors == "raise":
                    raise # reraises the last exception
                else:
                    pass
                continue
            total += row[2] * row[3]
    return total


print("Total Cost: ", portfolio_cost('missing.csv',errors='silent'))



import glob

files = glob.glob('portfolio*')
for file in files:
    portfolio_cost(file)
