#!/usr/bin/env python

import fileinput

for line in fileinput.input():
    print line.strip().split(".")

# The END
