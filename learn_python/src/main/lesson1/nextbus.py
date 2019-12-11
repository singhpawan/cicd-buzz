#!/usr/bin/env python3

import sys
import urllib.request
from xml.etree.cElementTree import XML


if len(sys.argv) != 3:
    raise SystemExit('Usage: nextbus.py route stopid')

route = sys.argv[1]
stop = sys.argv[2]
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route={}&stop={}'.format(
    route,stop))

data = u.read()
doc = XML(data)

import pdb; pdb.set_trace() # Launch Debugger ( Manual debugging / breakpoint)
for pt in doc.findall('.//pt'):
    print(pt.text)

