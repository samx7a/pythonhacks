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

inputstream     = get_input()
print(set(inputstream))
