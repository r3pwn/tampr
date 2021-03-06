#!/usr/bin/env python3
import subprocess
import sys
import argparse

parser = argparse.ArgumentParser(prog='{} stat'.format(sys.argv[0]), 
            description='view some data of standard files', add_help=False)

def main(args):
    stat_file(args[2])

def stat_file(filename):
    # tool file 'filename'
    process = subprocess.Popen(['stat', filename], 
                           stdout=subprocess.PIPE,
                           universal_newlines=True)

    while True:
        output = process.stdout.readline()
        print(output.strip())
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            # Process has finished, read rest of the output 
            for output in process.stdout.readlines():
                print(output.strip())
            break

def short_desc():
    print("  stat - " + parser.description)

def help():
    parser.print_help()
