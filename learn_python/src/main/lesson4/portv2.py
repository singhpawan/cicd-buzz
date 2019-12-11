#!/usr/bin/env python3

import csv
import sys

def portfolio_cost(filename):
    '''
    Computes total shares*price for a csv file with name,date,shares,price data
    :param filename:
    :return: the total value of the portfolio
    '''
    total = 0.0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        header = next(f)
        for rowno, row in enumerate(rows, start=1):
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err: # extra qualifier as ( this will store the exception in the variable)
                print("Row", rowno, "Bad Row:", row)
                print("Reason", err)
                continue # this will skip the iteration since we have a bad input.
            total += row[2] * row[3]
    return total


print("Total Cost: ", portfolio_cost(sys.argv[1]))



import glob

files = glob.glob('portfolio*')
for file in files:
    portfolio_cost(file)