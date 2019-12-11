
# reader.py

import sys
import csv


def read_csv(filename, types, *, errors='warn'):
    '''
    Read a csv with type conversion into a list name, date, share , price data into a list
    '''

    if errors not in {'warn', 'silent', 'raise'}:
        raise ValueError("errors must be one of 'warn, 'silent,' 'raise'")

    records = []
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            try:
                row = [func(val) for func, val in zip(types,row)]
            except ValueError as err:
                if errors == 'warn':
                    print('Row:', rowno, 'Bad row:', row)
                    print('Rowno', rowno, 'Reason',err)
                elif errors == 'raise':
                    raise
                else:
                    pass # Ignore
            record = dict(zip(headers,row))
            records.append(record)
    return records



'''
This function is now not tied to a portfolio or stocks but is generalized to all types of files.
'''

