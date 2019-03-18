import sys, getopt, glob, os, fnmatch, re
import argparse
import subprocess
from subprocess import Popen, PIPE
def get_args():
    ap = argparse.ArgumentParser()
    # Positional argument for search pattern.
    ap.add_argument("search_pattern",
            help="String or regex pattern to search for in file."
            )
    # Positional argument for files to search. Can be multiple files.
    ap.add_argument('files', 
            help="File name, or file pattern to search for given term.",
            nargs='*'
            )
    args = vars(ap.parse_args())
    return args

args            = get_args()
search_pattern  = args['search_pattern']
files           = args['files']

matching_lines = []
reg = re.compile(search_pattern)
for filename in files:
    with open(filename) as f:
        lines= f.readlines()
        linecount = 0
        for line in lines:
            if (reg.search(line)):
                print "%s:%d:%s" % (filename, linecount, line)


