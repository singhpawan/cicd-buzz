# holding.py

import csv

class Holding(object):
    def __init__(self, name, date, shares, price):
        self.name  = name
        self.date = date
        self.shares = shares
        self.price = price

    def cost(self):
        return self.price * self.shares

    def sell(self, nshares):
        self.shares -= nshares


def read_portfolio(filename):
    portfolio = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(f)
        for row in rows:
            h = Holding(row[0], row[1], int(row[2]), float(row[3]))
            portfolio.append(h)
    return portfolio



