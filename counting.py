#!/usr/bin/python

def count_letters(string):
    if not len(string):
        return ""
    out = ''
    count = 0
    previous = string[0]
    string += '\r' # Add EOL
    for l in string:
        if l == previous:
            count += 1
        elif count:
            out += str(count) + previous
            count = 1
        previous = l
    return out

print count_letters('aaaaabbbbccccccaaaaaaa')