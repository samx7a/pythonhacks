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
    # Optional argument containing command for sed to execute
    ap.add_argument("-e",
            help="-e provides argument containing command to be executed by sed"
            )
    args = vars(ap.parse_args())
    return args

args            = get_args()
inputstream     = get_input()
command         = args['e']
commandpattern  = re.compile('^s\/(.*)\/(.*)\/(g?)')


# Handle sub command from -e. begins with s/_/_/.
# Delimiter is slash
commandsplit    = commandpattern.match(command)
searchpattern   = commandsplit.group(1)
replace         = commandsplit.group(2)
global_flag     = commandsplit.group(3)

searchregex = re.compile(searchpattern) 
for line in inputstream:
    if global_flag:
        print searchregex.sub(replace, line)
    else:
        print searchregex.sub(replace, line, 1)

