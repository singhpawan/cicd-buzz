#!/usr/bin/env python3

# Take a look at the portfolio2.csv it has a , in the second field which breaks the previous code
# , is part of the data and it shouldn't be doing that.
# Using a csv module takes care of these issues.

# Takeaway: look out for standard library file format modules, it will greatly simplify the code

'''
If you are reading data and you are working with any kind of standard file encoding or anything like that, chances are
that there is some library module that can help you out. One of the libraries that Python provides is a library called
 CSV. The whole purpose of this library is to read commas separated value file
'''

# so if working with files, it's important to find the right library

import csv
total = 0.0
with open('portfolio2.csv', 'r') as f:
    rows = csv.reader(f) # puts a csv reader around the file.
    header = next(f)
    for row in rows:
       row[2] = int(row[2])
       row[3] = float(row[3])
       total += row[2] * row[3]

print("Total Cost: ", total)