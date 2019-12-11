
# import lesson6.reader # top level import
from . import reader # Package-relative import (This makes package name is not hardcoded)
import src.main.lesson6.reader




def read_portfolio(filename, *, errors ='warn'):
    return reader.read_csv(filename, [str, str, int, float], errors=errors)


if __name__ == '__main__':
    portfolio = read_portfolio('./../Data/portfolio.csv')
    total = 0.0
    for holding in portfolio:
        total += holding['shares'] * holding['price']
    print('Total Cost', total)