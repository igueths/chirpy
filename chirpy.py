#!/usr/bin/env python
import csv
import argparse
from collections import OrderedDict
# Define our command line arguments and parse them.
def parse_arguments():
    args = argparse.ArgumentParser(description='Manipulates Chirp-exported CSV files from the command line')
    args.add_argument('csvfile', help='The filename of the CSV file we wish to use')
    args.add_argument('outfile', help='The output CSV file we wish to write our output to.
    args.add_argument('-l', '--location', help='The memory location in the radio for an entry', type=int)
    args.add_argument('-n', '--name', help='Name of this memory entry')
    args.add_argument('-f', '--frequency', help='Frequency associated with a memory location')
    args.add_argument('-d', '--duplex', help='Duplex of our signal; supported values (+ | -)')
    args.add_argument('-o', '--offset', help='Offset between input and output frequencies, one should not usually have to change this', default=0.600000)
    args.add_argument('-t', '--tonemode', help='Tone mode (PL | CTCSS | DTCS)', dest='tonemode', choices=['Tone', 'TSQL', 'DTCS'])
    args.add_argument('-T', '--rtonefreq', help='PL tone frequency, cannot be used unless mode tone is specified')
    args.add_argument('-c', '--ctonefreq', help='CTCSS tone frequency, cannot be used unless "TSQL" is passed to --tone')