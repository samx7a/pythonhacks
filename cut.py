import sys, getopt, glob, os, fnmatch, re
import argparse
import subprocess
from subprocess import Popen, PIPE
def get_input():
    try:
        while True:
            yield raw_input()
    except EOFError:
        raise StopIteration

def get_fields(fieldranges):
    fields = []
    ranges = fieldranges.split(',')
    # handle ranges specified with dashes.
    for fieldrange in ranges:
        if('-' in fieldrange):
            lower, upper = fieldrange.split('-')
            for i in range(int(lower), int(upper) + 1):
                fields.append(i)
        else:
            # handle single fields separated by commas
            fields.append(int(fieldrange))
        
    return fields

# We can take input from std in. We take options from command line args.
_, delimiter, fields = sys.argv

fields = get_fields(fields)
inputlines  = get_input()
for line in inputlines:
    inputfields = line.split(delimiter)
    for field in fields:
        try:
            print inputfields[field]
        except: 
            pass

