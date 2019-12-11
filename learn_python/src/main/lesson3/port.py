#!/usr/bin/env python3

# port.py

total = 0.0
with open('portfolio.csv','r') as f:
    headers = next(f) # skip a line (since the logic won't work on the header)
    for line in f:
        line = line.strip() # strip whitespace
        parts = line.split(',')
        parts[0] = parts[0].strip('"')
        parts[1] = parts[1].strip('"')
        parts[2] = int(parts[2])
        parts[3] = float(parts[3])
        total += parts[2] * parts[3]


print("Total Cost: ", total)




"""
Step 1: open a file
Step 2: go line by lind
Step 3: perform some computation
Step 4 exit the file
"""