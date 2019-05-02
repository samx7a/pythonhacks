import sys, getopt, glob, os, fnmatch, re
import argparse
import subprocess
from subprocess import Popen, PIPE
def get_args():
    ap = argparse.ArgumentParser()
    # optional name filter argument
    ap.add_argument("-n", "--name", 
            help="A filter on the name of files to be returned by find"
            )
    # optional file type filter argument
    ap.add_argument("-t", "--type",
            help="A filter on the type of files to be returned by find. e.g. d is directories, f is files"
            )
    # optional argument to perform an action on each matching file
    ap.add_argument("--exec",
            help="Execute shell command on each matching file. {} replaces filename. Command is terminated by \;"
            )
    # positional path argument compulsory
    ap.add_argument('path',
            )
    args = vars(ap.parse_args())
    return args

def filter_by_name(name, files):
    for filename in files:
        if fnmatch.fnmatch(filename, name):
            yield filename

def filter_by_type(filetype, files):
    if filetype == 'd':
        for filename in files:
            if os.path.isdir(filename):
                yield filename
    if filetype == 'f':
        for filename in files:
            if os.path.isfile(filename):
                yield filename

args = get_args()
path = args['path']
name = args['name']
filetype = args['type']
command = args['exec']

files = os.listdir(path)

# Filter by name?
if name: 
    files = filter_by_name(name, files)
# Filter by type of file (directory or file)
if filetype:
    files = filter_by_type(filetype, files)

if command:
    for filename in files:
        # Substitue filename
        commandString = command.replace("{}", filename)
        # Trim backslash semi-colon from command
        pattern = '(.*)\\\;'
        m = re.search(pattern, commandString)
        commandString = m.group(1)
        print "SH: Here is the command string to execute %s\n" % commandString
        subprocess.Popen(commandString, stdout=PIPE, shell=True).stdout.read()
else: 
    for filename in files:
        print filename
