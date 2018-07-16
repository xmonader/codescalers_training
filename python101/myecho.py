#!/usr/bin/env python3
import sys

# print(sys.argv)
scriptname = sys.argv[0]

for arg in sys.argv[1:]:
    print(arg, end=" ")

