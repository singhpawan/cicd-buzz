#!/usr/bin/env python3

import csv
import sys

# Function takes an input, does some computation and the returns the value.
# Function gives structure to your program and enables reusability.
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
        for row in rows:
            row[2] = int(row[2])
            row[3] = float(row[3])
            total += row[2] * row[3]
        return total

print("Total Cost: ", portfolio_cost(sys.argv[1]))


# Glob let's you grab file names that match a specific pattern.
import glob

files = glob.glob('portfolio*')
for file in files:
    portfolio_cost(file)