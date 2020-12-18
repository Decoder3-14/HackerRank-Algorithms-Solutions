#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    result = s.replace('AM', '')
    result = result.replace('PM', '')
    sections = result.split(':')
    first_section = int(sections[0])
    if first_section < 12 and 'PM' in s:
        sections[0] = str(first_section + 12)
        if sections[0] == '0':
            sections[0] = '00'
    if first_section >= 12 and 'AM' in s:
        sections[0] = str(first_section - 12)
        if sections[0] == '0':
            sections[0] = '00'
    result = ':'.join(sections)
    return result

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
