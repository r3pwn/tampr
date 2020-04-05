#!/usr/bin/env python3
import sys
import argparse

parser = argparse.ArgumentParser(prog='{} test'.format(sys.argv[0]), 
            description='this is a test command', add_help=False)
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

def main(args):
    args = parser.parse_args()

def short_desc():
    print("  test - " + parser.description)

def help():
    parser.print_help()

