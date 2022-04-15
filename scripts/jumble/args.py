#!/usr/bin/python3

import random
import sys

#raw = sys.argv[1]]
try:
  arg = sys.argv[1]
except IndexError:
  arg = None

if arg == None:
    print("Starting in normal mode.")

else:
    print(arg)

