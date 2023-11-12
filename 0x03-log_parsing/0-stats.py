#!/usr/bin/python3

import sys
import os


statusDict = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
inputSplit = []
count = 0

try:
    for line in sys.stdin:
        inputSplit = line.split(" ")
        status_input = int(inputSplit[-2])
        file_size = int(inputSplit[-1].split("\n")[0])
        print(status_input, file_size)
except KeyboardInterrupt:
    print("keyboard interrupt")
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
