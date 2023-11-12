#!/usr/bin/env python

import sys
import os

try:
  for line in sys.stdin:
    print(line)
except KeyboardInterrupt:
  print('keyboard interrupt')
  try:
    sys.exit(0)
  except SystemExit:
    os._exit(0)
