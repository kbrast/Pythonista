#!/usr/bin/env python3
# Generate a list of files in the current working directory
# Sort by filename and specify filesize in bytes

import os
CurrentDir = os.getcwd()
Files = sorted(os.listdir(CurrentDir))

cwdDict = dict()
for Info in Files:
    Stats = os.stat(Info)
    cwdDict[Info] = Stats

for item in cwdDict:
    print("{:40s} {:d} bytes".format(item,cwdDict[item].st_size))
