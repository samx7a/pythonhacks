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

def get_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("-r",
            help="Flag to reverse output of sorted list.",
            action="store_true"
            )
    ap.add_argument("-n",
            help="Flag to sort list on numeric value.",
            action="store_true"
            )
    args = vars(ap.parse_args())
    return args

args            = get_args()
inputstream     = get_input()
reverse         = args['r'] | False
numeric_sort    = args['n']

if numeric_sort:
    print sorted(inputstream, key=int, reverse=reverse)
else:
    print sorted(inputstream, reverse=reverse)
